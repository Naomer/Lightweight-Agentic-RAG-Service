import os
import json
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from app.schemas import AnalyzeRequest, AnalyzeResponse 
from app.services.llm_service import generate_answer
from app.services.retrieval_service import RetrieverService

# 1. Environment Validation (The Smoke Test)
load_dotenv()
if not os.getenv("GROQ_API_KEY"):
    # The app won't even start if the key is missing
    raise RuntimeError("CRITICAL: GROQ_API_KEY is not set in environment or .env file")

# 2. Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Agentic Lead RAG")
retriever = RetrieverService()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    logger.info("--- New Request Received ---")
    logger.info(f"Query: {request.text}")

    try:
        # 3. Retrieval Step
        retrieved_chunks = retriever.retrieve(request.text, k=5)
        logger.info(f"FAISS retrieved {len(retrieved_chunks)} chunks")

        # Handles both simple text and dictionary chunks (for future metadata)
        context = "\n".join([chunk["text"] if isinstance(chunk, dict) else chunk for chunk in retrieved_chunks])

        # 4. LLM Generation Step
        logger.info("Sending context to Groq...")
        raw_answer = await generate_answer(context, request.text)
        logger.info(f"Raw Groq Response: {raw_answer}")

        # 5. Parsing and Validation
        parsed_answer = json.loads(raw_answer)
        
        response_data = {
            "question": request.text,
            "context_used": retrieved_chunks,
            "analysis": parsed_answer
        }
        
        logger.info("Analysis successfully parsed and validated.")
        return response_data

    except json.JSONDecodeError:
        logger.error(f"CRITICAL: Groq returned non-JSON string: {raw_answer}")
        raise HTTPException(status_code=502, detail="AI returned invalid JSON format")
    except Exception as e:
        # This catches schema mismatches (missing fields like 'reasoning')
        logger.error(f"Validation or System Error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=422, detail=f"Data error: {str(e)}")

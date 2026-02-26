import os
import json
from dotenv import load_dotenv  
from groq import AsyncGroq 

load_dotenv() 

client = AsyncGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    timeout=300.0, 
    max_retries=5
)

async def generate_answer(context, user_query):
    system_prompt = """
    You are a startup lead intelligence AI agent.
    Analyze the provided context and return structured JSON ONLY.

    CRITICAL RULES:
    - Focus ONLY on the company that matches the user's specific role request.
    - Extract the "Source" URL if it exists in the context (it follows the ' | Source: ' tag).
    - If no URL is found, return "Unknown".

    You MUST include these exact keys in your JSON:
    1. "startup_name": (The name of the company or "Unknown")
    2. "hiring_signal": (true or false)
    3. "remote_possible": (true or false)
    4. "funding_stage": (e.g., "seed", "series_a", "unknown")
    5. "reasoning": (One sentence explaining why this company is the best lead)
    6. "source_url": (The URL found in the context for this specific lead)

    Return valid JSON only.
    """

    user_prompt = f"Context:\n{context}\n\nUser Query:\n{user_query}"

    response = await client.chat.completions.create(
        model="llama-3.1-8b-instant",
        # Try 70b-versatile for smarter reasoning, or keep 8b-instant for speed
        # model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.1, 
        response_format={"type": "json_object"} 
    )

    # Note: Added [0] index to avoid the error in the logs
    return response.choices[0].message.content

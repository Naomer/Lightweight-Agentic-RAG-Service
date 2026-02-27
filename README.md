## Lightweight Agentic RAG Service

---

## 🚀 Agentic Lead Intelligence RAG

A lightweight, production-ready Agentic RAG (Retrieval-Augmented Generation) service that analyzes startup signals (hiring, funding, remote readiness) using semantic search + LLM reasoning.

Built with:
 • FastAPI
 • FAISS (vector search)
 • Sentence Transformers
 • Groq LLM (Llama 3.3 70B)
 • Docker-ready architecture

---

## 🧠 What This Project Does

## This service:
 1. Embeds startup-related signals into a FAISS vector store
 2. Retrieves the most relevant context using semantic similarity
 3. Sends structured context to an LLM
 4. Returns structured JSON analysis

Example analysis output:
```bash
{
  "startup_name": "ExampleAI",
  "hiring_signal": true,
  "remote_possible": true,
  "funding_stage": "Seed",
  "reasoning": "Raised seed round and actively hiring Flutter developer.",
  "source_url": "https://example.com/post"
}
```

---

## 🏗 Architecture
```bash
User Query
    ↓
Retriever (FAISS + Embeddings)
    ↓
Context Assembly
    ↓
Groq LLM (Structured JSON Output)
    ↓
FastAPI Response
```
## Components:
 • embedding_service.py → Generates sentence embeddings
 • vector_store.py → FAISS index + persistence
 • retrieval_service.py → Semantic retrieval logic
 • llm_service.py → Groq structured JSON generation
 • main.py → FastAPI endpoints

---

## ⚙️ Tech Stack
 ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) Python 3.10+  
 ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) FastAPI  
 ![FAISS](https://img.shields.io/badge/FAISS-0D0D0D?logo=faiss&logoColor=white) FAISS (CPU)  
 ![SentenceTransformers](https://img.shields.io/badge/SentenceTransformers-2C3E50?logo=python&logoColor=white) SentenceTransformers (all-MiniLM-L6-v2)  
 ![Groq](https://img.shields.io/badge/Groq-FF6F61?logo=groq&logoColor=white) Groq LLM API  
 ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) Docker

---

🚀 Getting Started

## 1️⃣ Clone
```bash
git clone https://github.com/Naomer/agentic-lead-rag.git
cd agentic-lead-rag
```

---

## 2️⃣ Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment

Create .env file:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

---

## 5️⃣ Run the API
```bash
uvicorn app.main:app --reload
```
Open:

http://127.0.0.1:8000/docs

Use /analyze endpoint.

---

## 🐳 Docker Support
Dockerized FastAPI agent for RAG tasks.

## Run locally with Docker

Build image:
```bash
docker build -t agentic-lead-rag .
```
Run container:
```bash
docker run -p 8000:8000 --env-file .env agentic-lead-rag
```

Visit: http://localhost:8000/docs


---

## 📦 Features
 • Structured JSON enforcement from LLM
 • Async Groq integration
 • Semantic search retrieval
 • Source URL tracking
 • FAISS index persistence
 • Dockerized for portability

---

## 🔬 Example Query
```bash
"Startup hiring Flutter developer remotely after seed funding"
```
Returns structured intelligence analysis based on stored signals.

---

## 🧭 Roadmap
 • Live Reddit & X ingestion
 • LinkedIn signal scraping
 • Scheduled background refresh
 • Frontend dashboard
 • Multi-source ingestion pipeline
 • Deployment (Render / Railway)
 • Usage-based monetization

---

## 🎯 Why This Matters

## This is not a chatbot.

It is a structured intelligence engine designed to extract startup signals for:
 • Freelancers
 • Recruiters
 • Founders
 • Investors

---

## 🧱 Author

Built by Me — AI-focused mobile + systems engineer exploring Agentic architectures and applied intelligence systems.

---

## 📄 License

MIT License

---


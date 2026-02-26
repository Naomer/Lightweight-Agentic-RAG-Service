# Lightweight Agentic Lead Intelligence RAG Service

### Production-ready RAG microservice for domain-specific knowledge retrieval.

## AI systems that help startups discover and act on revenue opportunities.

# Lightweight Agentic RAG Service

Dockerized FastAPI agent for RAG tasks.

## Run locally with Docker

```bash
docker build -t lead-rag-agent .
docker run -d -p 8000:8000 --env-file .env -v "${PWD}:/app" lead-rag-agent
```

Visit: http://localhost:8000/docs


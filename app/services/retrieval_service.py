from app.services.embedding_service import embed_text
from app.services.vector_store import add_to_index, search_index, index # Import 'index'
from pathlib import Path

class RetrieverService:
    def __init__(self):
        self._load_knowledge()

    def _load_knowledge(self):
        if index.ntotal > 0:
            print(f"--- FAISS: Index already loaded with {index.ntotal} items. ---")
            return

        knowledge_path = Path("app/data/knowledge.txt")
        if knowledge_path.exists():
            print("--- FAISS: Index empty. Loading with URL support... ---")
            with open(knowledge_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    
                    if " | " in line:
                        # Split text and url
                        text, url = line.split(" | ", 1)
                        embedding = embed_text(text)
                        # We store both so the LLM can find the URL later
                        add_to_index(embedding, f"Lead: {text} | Source: {url}")
                    else:
                        add_to_index(embed_text(line), line)

    def retrieve(self, query, k=3):
        query_embedding = embed_text(query)
        return search_index(query_embedding, top_k=k)

class AgentService:
    def __init__(self, llm, embedder, retriever):
        self.llm = llm
        self.embedder = embedder
        self.retriever = retriever

    def answer(self, query: str):
        results = self.retriever.search(query)
        return {"query": query, "results": results}

import os
from document_manager import document_manager
from config import config
from logger import logger

class RAGManager:
    def __init__(self):
        self.enabled = config.RAG_ENABLED

    def query_context(self, query: str) -> str:
        """Lightweight context extraction from uploaded docs"""
        if not self.enabled:
            return ""

        docs = document_manager.list_documents()
        extracted_contexts = []

        for doc in docs:
            doc_path = os.path.join("uploads", doc)
            try:
                if doc.endswith(".txt") or doc.endswith(".md"):
                    with open(doc_path, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                        if any(q.lower() in text.lower() for q in query.split()):
                            # Return relevant snippet
                            extracted_contexts.append(text[:1000])
            except Exception as e:
                logger.error(f"Error reading doc {doc}: {e}")

        return "\n---\n".join(extracted_contexts)

rag_manager = RAGManager()

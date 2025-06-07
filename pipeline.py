
from viarag.core.ingestion import SimpleTextIngestor
from viarag.embed.remote_embedder import RemoteEmbedder
from viarag.retrieve.remote_retriever import RemoteRetriever

class ViaRAG:
    def __init__(self, base_url: str, api_key: str = None):
        self.ingestor = SimpleTextIngestor()
        self.embedder = RemoteEmbedder(base_url, api_key=api_key)
        self.retriever = RemoteRetriever(base_url, api_key=api_key)

    def ingest_and_embed(self, path: str):
        docs = self.ingestor.ingest(path)
        return self.embedder.embed(docs)

    def search(self, query: str, prefix: str = "", suffix: str = ""):
        return self.retriever.query(query, prefix, suffix)

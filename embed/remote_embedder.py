
import requests
from typing import List, Optional, Dict
from viarag.core.document import Document

class RemoteEmbedder:
    def __init__(self, base_url: str, embedder: str = "openai", vector_store: str = "qdrant", embedder_config: Optional[Dict] = None, api_key: Optional[str] = None):
        self.url = base_url.rstrip("/") + "/embed"
        self.embedder = embedder
        self.vector_store = vector_store
        self.embedder_config = embedder_config
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

    def embed(self, documents: List[Document]) -> Dict:
        payload = {
            "files": [doc.content for doc in documents],
            "embedder": self.embedder,
            "vector_store": self.vector_store,
            "embedder_config": self.embedder_config,
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

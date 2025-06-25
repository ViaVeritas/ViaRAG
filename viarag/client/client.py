"""
ViaRAGClient: Main entry point for using the ViaRAG SDK.

- Initialize ViaRAGClient with your base_url and api_key.
- Use query(), direct_query(), match_context() for RAG operations.
- Use upload_files() to add documents, chunk_text() to split text, health() to check service.
- Start here for most SDK tasks.
"""
from typing import Optional, List
from viarag.core.http import ViaRAGHTTPClient
from viarag.core.models import QueryInput, ChunkInput

class ViaRAGClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.client = ViaRAGHTTPClient(base_url, api_key)

    def query(self, prompt: str):
        return self.client.post("/api/v1/simple/query", QueryInput(prompt=prompt).dict())

    def direct_query(self, prompt: str):
        return self.client.post("/api/v1/simple/query/direct", QueryInput(prompt=prompt).dict())

    def match_context(self, prompt: str):
        return self.client.post("/api/v1/simple/query/match", QueryInput(prompt=prompt).dict())

    def upload_files(self, file_paths: List[str]):
        return self.client.upload("/api/v1/simple/upload", file_paths)

    def chunk_text(self, text: str, chunk_size: int = 500, chunk_overlap: int = 50):
        return self.client.post("/api/v1/simple/chunk", ChunkInput(text=text, chunk_size=chunk_size, chunk_overlap=chunk_overlap).dict())

    def health(self):
        return self.client.get("/api/v1/simple/health")

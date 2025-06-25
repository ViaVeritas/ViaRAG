"""
Pydantic models for ViaRAG SDK API requests and responses.

- QueryInput: For sending queries to the API.
- ChunkInput: For splitting text into chunks.
- UploadResult: For upload responses.
- Used by ViaRAGClient methods.
"""
from pydantic import BaseModel
from typing import Optional, List

class QueryInput(BaseModel):
    prompt: str

class ChunkInput(BaseModel):
    text: str
    chunk_size: int = 500
    chunk_overlap: int = 50

class UploadResult(BaseModel):
    file_name: str
    success: bool

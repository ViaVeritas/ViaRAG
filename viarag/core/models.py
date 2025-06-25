
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

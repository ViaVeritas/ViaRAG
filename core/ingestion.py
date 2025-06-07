
import os
from .document import Document

class SimpleTextIngestor:
    def ingest(self, path: str):
        docs = []
        for file in os.listdir(path):
            if file.endswith(".txt"):
                with open(os.path.join(path, file), "r") as f:
                    docs.append(Document(content=f.read()))
        return docs

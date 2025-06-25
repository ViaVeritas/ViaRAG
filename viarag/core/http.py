"""
ViaRAGHTTPClient: Handles all HTTP requests for the SDK.

- Used internally by ViaRAGClient; you usually don't need to use this directly.
- Provides get(), post(), and upload() methods for API communication.
"""

import requests
from typing import Optional, List

class ViaRAGHTTPClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

    def get(self, path: str):
        response = requests.get(self.base_url + path, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def post(self, path: str, payload: dict):
        response = requests.post(self.base_url + path, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def upload(self, path: str, file_paths: List[str]):
        files = [("file", open(path, "rb")) for path in file_paths]
        response = requests.post(self.base_url + path, headers=self.headers, files=files)
        for _, f in files:
            f.close()
        response.raise_for_status()
        return response.json()

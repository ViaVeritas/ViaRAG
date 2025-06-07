
import requests

class RemoteRetriever:
    def __init__(self, base_url: str, llm_provider: str = "openai", embedder: str = "openai", vector_store: str = "qdrant", api_key: str = None):
        self.url = base_url.rstrip("/") + "/query"
        self.llm_provider = llm_provider
        self.embedder = embedder
        self.vector_store = vector_store
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

    def query(self, prompt: str, prompt_prefix: str = "", prompt_suffix: str = ""):
        payload = {
            "prompt": prompt,
            "llm_provider": self.llm_provider,
            "embedder": self.embedder,
            "vector_store": self.vector_store,
            "prompt_prefix": prompt_prefix,
            "prompt_suffix": prompt_suffix,
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

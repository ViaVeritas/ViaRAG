
from pathlib import Path
import toml
import os
from typing import Optional

def load_config(path: Optional[str] = None):
    config_path = Path(path or os.getenv("VIARAG_CONFIG", "~/.viarag/config.toml")).expanduser()
    if config_path.exists():
        return toml.load(config_path)
    else:
        return {
            "default": {
                "base_url": os.getenv("VIARAG_BASE_URL", "https://viarag-backend-prod-104241861537.us-central1.run.app"),
                "api_key": os.getenv("VIARAG_API_KEY", None)
            }
        }

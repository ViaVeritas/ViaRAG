
# ViaRAG SDK

A structured Python SDK for interacting with the ViaRAG `/api/v1/simple/*` endpoints.

## Features

- Upload files and chunk text
- Query and match context from a vector store
- Health checking, chunking, and configurable API access
- Works with Supabase and other backends

## Install (from PyPI)

```bash
pip install viarag-sdk
```

## Install (from source)

```bash
git clone https://github.com/ViaVeritas/ViaRAG_SDK.git
cd ViaRAG_SDK
pip install .
```

## Usage Example

```python
from viarag.client.client import ViaRAGClient

client = ViaRAGClient(
    base_url="https://viarag-backend-prod-104241861537.us-central1.run.app",
    api_key="sk-your-key"
)

# Query
print(client.query("What is ViaRAG?"))

# Upload files
print(client.upload_files(["example.pdf"]))

# Chunk text
print(client.chunk_text("This is a long text...", chunk_size=300, chunk_overlap=30))

# Health check
print(client.health())
```

## Configuration

You can create a config file at `~/.viarag/config.toml`:

```toml
[default]
base_url = "https://viarag-backend-prod-104241861537.us-central1.run.app"
api_key = "sk-your-key"
```

## License

[GNU GPL v3](LICENSE)


import argparse
from viarag.pipeline import ViaRAG

def main():
    parser = argparse.ArgumentParser(description="ViaRAG CLI")
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--api-key", required=True)
    parser.add_argument("--docs", help="Path to .txt files to embed")
    parser.add_argument("--query", help="Query string for retrieval")

    args = parser.parse_args()

    rag = ViaRAG(base_url=args.base_url, api_key=args.api_key)

    if args.docs:
        print("Ingesting and embedding documents...")
        result = rag.ingest_and_embed(args.docs)
        print(result)

    if args.query:
        print("Running query...")
        result = rag.search(args.query)
        print(result)

if __name__ == "__main__":
    main()

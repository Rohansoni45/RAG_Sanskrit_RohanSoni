# app_cli.py
from rag_pipeline import build_index, answer_query

def main():
    collection = build_index()
    print("Ready. Type 'exit' to quit.")
    while True:
        q = input("Query> ").strip()
        if q.lower() in ("exit", "quit"):
            break
        result = answer_query(q, collection, k=3)
        print("=== Model output ===")
        print(result)

if __name__ == "__main__":
    main()

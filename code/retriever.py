# retriever.py

def retrieve_top_k(collection, query, k=3):
    """
    Retrieve top-k similar chunks using ChromaDB collection.
    """
    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    # Chroma returns dict: ids, documents, distances
    ids = results["ids"][0]
    docs = results["documents"][0]
    scores = results["distances"][0]

    return list(zip(ids, docs, scores))

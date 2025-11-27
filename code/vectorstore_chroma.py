# vectorstore_chroma.py

import chromadb
from chromadb.utils import embedding_functions

# Create persistent client
client = chromadb.PersistentClient(path="./chroma_db")

def create_collection(name="sanskrit_rag"):
    if name in [c.name for c in client.list_collections()]:
        return client.get_collection(name)
    return client.create_collection(name)

def add_documents(collection, ids, documents, embeddings):
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

def get_collection(name="sanskrit_rag"):
    return client.get_collection(name)

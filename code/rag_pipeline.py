# rag_pipeline.py
from loader import load_docx_text
from preprocess import basic_cleanup
from chunker import chunk_text_by_words
from embedder import load_embedder, embed_texts
from vectorstore_chroma import create_collection, add_documents
from retriever import retrieve_top_k
from generator_ollama import generate_with_ollama
import uuid

# CORRECT PATH (choose ONE)
DATA_PATH = r"D:\RAG_Sanskrit_RohanSoni\data\Rag-docs-fixed.docx"

# OR
# DATA_PATH = "../data/Rag-docs.docx"

def build_index():
    text = load_docx_text(DATA_PATH)
    text = basic_cleanup(text)
    chunks = chunk_text_by_words(text, chunk_size=300, overlap=50)
    embed_model = load_embedder()
    embeddings = embed_texts(embed_model, chunks, batch_size=16)
    coll = create_collection("sanskrit_rag")
    ids = [str(uuid.uuid4()) for _ in chunks]
    add_documents(coll, ids, chunks, embeddings.tolist())
    return coll

def answer_query(query, collection, k=3):
    top = retrieve_top_k(collection, query, k=k)
    context = "\n\n".join([doc for (_id, doc, _score) in top])
    prompt = f"""You are a helpful assistant. Use the context below (Sanskrit) to answer the user query in Sanskrit if user asked in Sanskrit, otherwise in English.\n\nContext:\n{context}\n\nUser question: {query}\n\nAnswer:"""
    resp = generate_with_ollama(prompt, stream=False)
    return resp

if __name__ == "__main__":
    coll = build_index()
    print("Index built. Ready to query.")
    q = input("Enter query: ")
    print(answer_query(q, coll))

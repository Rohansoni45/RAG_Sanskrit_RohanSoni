# embedder.py
import os
os.environ["USE_TF"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

def load_embedder():
    model = SentenceTransformer(MODEL_NAME)
    return model

def embed_texts(model, texts, batch_size=32):
    embeddings = model.encode(texts, show_progress_bar=True, batch_size=batch_size)
    return np.array(embeddings)

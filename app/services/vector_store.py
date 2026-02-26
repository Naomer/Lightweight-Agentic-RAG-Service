import faiss
import numpy as np
import os
import pickle

DIMENSION = 384
INDEX_PATH = "app/data/faiss.index"
TEXTS_PATH = "app/data/stored_texts.pkl"

# Load or create index
if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
else:
    index = faiss.IndexFlatL2(DIMENSION)

# Load stored texts
if os.path.exists(TEXTS_PATH):
    with open(TEXTS_PATH, "rb") as f:
        stored_texts = pickle.load(f)
else:
    stored_texts = []

def save_index():
    faiss.write_index(index, INDEX_PATH)
    with open(TEXTS_PATH, "wb") as f:
        pickle.dump(stored_texts, f)

def add_to_index(embedding, text):
    vector = np.array([embedding]).astype("float32")
    index.add(vector)
    stored_texts.append(text)
    save_index()

def search_index(query_embedding, top_k=3):
    if index.ntotal == 0:
        return []

    query_vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(stored_texts):
            results.append(stored_texts[idx])

    return results
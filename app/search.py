import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.embeddings import generate_embeddings

model = SentenceTransformer("clip-ViT-B-32")

embeddings, image_paths = generate_embeddings()

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def search_images(query, top_k=5):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding), top_k
    )

    results = []

    for idx in indices[0]:
        results.append(image_paths[idx])

    return results
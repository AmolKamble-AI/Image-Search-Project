import os
import numpy as np
from PIL import Image
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("clip-ViT-B-32")

def generate_embeddings(image_folder="data/images"):

    embeddings = []
    image_paths = []

    for img in os.listdir(image_folder):

        path = os.path.join(image_folder, img)

        try:
            image = Image.open(path)
            emb = model.encode(image)

            embeddings.append(emb)
            image_paths.append(path)

        except:
            print("Skipping file:", img)
            continue

    return np.array(embeddings), image_paths

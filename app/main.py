from fastapi import FastAPI
from app.search import search_images
from app.explanation import generate_explanation

app = FastAPI(title="AI Image Search API")

@app.get("/search")

def search(query: str):

    images = search_images(query)

    results = []

    for img in images:

        explanation = generate_explanation(query, img)

        results.append({
            "image": img,
            "explanation": explanation
        })

    return {"results": results}
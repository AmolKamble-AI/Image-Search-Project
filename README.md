# AI Image Search System

An AI-powered image search system that allows users to search images using natural language queries.  
The system uses deep learning embeddings and similarity search to retrieve relevant images.

---

## Features

- Search images using text queries (e.g., "dog", "mountain")
- Uses CLIP model for semantic understanding of images and text
- Fast similarity search using FAISS
- REST API built with FastAPI
- Test cases using Pytest
- Docker support for containerization

---

## Project Structure

image-search-system
│
├── data
│ ├── photos_url.csv
│ └── images
│
├── scripts
│ └── download_images.py
│
├── app
│ ├── main.py
│ ├── embeddings.py
│ ├── search.py
│ ├── explanation.py
│
├── notebooks
│ └── experiment.ipynb
│
├── tests
│ └── test_api.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

Create Virtual Environment
python -m venv venv
Create Virtual Environment

Install Dependencies
pip install -r requirements.txt

Download Images
python scripts/download_images.py

THEN APPY RAG ARCH.

# RAG (Retrieval-Augmented Generation) System for Document Handling

This project implements a **RAG-based system** that allows users to query large documents and receive intelligent, context-aware answers using AI.

It combines:

- Document ingestion
- Semantic search (retrieval)
- LLM-based answer generation

Run the API
uvicorn app.main:app --reload
http://127.0.0.1:8000/docs

API Usage
GET /search?query=dog
Get Response FastAPI (http://127.0.0.1:8000/docs)
{
"results": [
{
"image": "data/images/dog.jpg",
"explanation": "The image is relevant to the query..."
}
]
}

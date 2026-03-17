# Import TestClient from FastAPI
# TestClient allows us to test our API without running the server in a browser
from fastapi.testclient import TestClient

# Import the FastAPI application we created in main.py
# "app" is the FastAPI object that contains our API endpoints
from app.main import app


# Create a testing client for the FastAPI app
# This client will simulate HTTP requests like a browser
client = TestClient(app)


# Create a test function
# pytest automatically runs functions that start with "test_"
def test_search():

    # Send a GET request to the API endpoint
    # This simulates opening this URL:
    # http://localhost:8000/search?query=dog
    response = client.get("/search?query=dog")

    # Check if the API response status is 200
    # 200 means the request was successful
    assert response.status_code == 200
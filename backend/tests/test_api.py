from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message" : "Welcome to SiteSense API!"
    }

def test_invalid_url():
    response = client.post(
        "/analyze",
        json= {
            "url": "hello"
        },
    )
    assert response.status_code == 422

def test_missing_url():
    response = client.post(
        "/analyze",
        json={},
    )

    assert response.status_code == 422
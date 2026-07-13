from fastapi.testclient import TestClient
from app import app
from unittest.mock import patch

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

def test_analyze_success():
    fake_result = {
        "fetch":{
            "url" : "https://example.com",
            "status_code": 200,
            "response_time": 0.2,
            "headers":{
                "Content-Type": "text/html"
            }
        },
        "seo":{
            "title": "Example Site",
            "title_length":12,
            "meta_description": "Example description",
            "meta_description_length": 100,
            "h1_count":1,
            "h2_count":0,
            "word_count":300
        },
        "score":{
            "score": 95,
            "grade":"A",
            "recommendations":[]
        }
    }

    with patch(
        "app.analyze",
        return_value= fake_result,
    ):
        response = client.post(
            "/analyze",
            json={
                "url":"https://example.com"
            }
        )
        assert response.status_code ==200
        data = response.json()
        assert data["fetch"]["url"] == "https://example.com"
        assert data["score"]["score"] == 95
        assert data["score"]["grade"] == "A"
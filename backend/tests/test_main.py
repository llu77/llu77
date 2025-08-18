import os
import sys
from fastapi.testclient import TestClient

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from app.main import app

client = TestClient(app)


def test_chat():
    response = client.post("/chat", json={"message": "hi"})
    assert response.status_code == 200
    assert response.json()["reply"] == "Echo: hi"

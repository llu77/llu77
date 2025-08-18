import os
import sys
from fastapi.testclient import TestClient

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from app.main import app

client = TestClient(app)


def test_chat():
    response = client.post("/chat", json={"message": "hi"})
    assert response.status_code == 200
    assert response.json()["reply"].startswith("Hello")


def test_history_endpoint():
    client.post("/chat", json={"message": "hi"})
    client.post("/chat", json={"message": "bye"})
    history = client.get("/history")
    assert history.status_code == 200
    data = history.json()
    assert len(data) >= 4  # user+bot for each chat
    assert data[0]["role"] == "user"
    assert data[1]["role"] == "bot"


def test_teach_and_use():
    teach = client.post("/teach", json={"trigger": "who are you", "response": "I am a bot"})
    assert teach.status_code == 200
    chat = client.post("/chat", json={"message": "Who are you?"})
    assert chat.status_code == 200
    assert chat.json()["reply"] == "I am a bot"

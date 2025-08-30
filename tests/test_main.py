# tests/test_main.py
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_item_success():
    response = client.get("/api/items/MLA123456")
    assert response.status_code == 200
    assert response.json()["title"] == "Smart TV 4K 55 pulgadas"

def test_read_item_not_found():
    response = client.get("/api/items/ID_INEXISTENTE")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}
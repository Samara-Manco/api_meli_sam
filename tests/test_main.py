# tests/test_main.py
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


# --- Prueas Originales ---

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


# --- Pruebas Adicionales (Deben pasar) ---

def test_read_second_item_success():
    """Prueba que la API puede encontrar correctamente el segundo item en los datos."""
    response = client.get("/api/items/MLA789012")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "MLA789012"
    assert data["title"] == "Laptop Gamer Core i7 16GB RAM"


def test_item_response_schema_and_types():
    """Prueba que la estructura y los tipos de datos del JSON de respuesta son correctos."""
    response = client.get("/api/items/MLA123456")
    assert response.status_code == 200
    data = response.json()

    # Verificar que los campos clave existan
    assert "id" in data
    assert "title" in data
    assert "price" in data
    assert "seller" in data

    # Verificar que los tipos de datos sean correctos
    assert isinstance(data["id"], str)
    assert isinstance(data["title"], str)
    assert isinstance(data["price"], float)
    assert isinstance(data["seller"], dict)

# def test_to_demonstrate_pipeline_failure():
    # """
    # Esta prueba está diseñada para fallar a propósito.
    # Pide un producto que existe (debería dar 200), pero comprueba si da un error 500.
    # Esto nos permite verificar que el pipeline de CI nos avisa cuando una prueba falla.
    # """
    # response = client.get("/api/items/MLA123456")
    # Afirmamos intencionalmente un resultado incorrecto para ver el pipeline fallar.
    # assert response.status_code == 500
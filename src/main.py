# src/main.py
import json
from fastapi import FastAPI, HTTPException
from pathlib import Path

app = FastAPI(
    title="API de Detalles de Producto",
    description="Una API para obtener detalles de productos al estilo MercadoLibre.",
    version="1.0.0"
)

# Construye la ruta al archivo de datos de forma segura
DATA_FILE = Path(__file__).parent.parent / "data" / "products.json"

def load_db():
    """Carga la base de datos de productos desde el archivo JSON."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

db = load_db()

@app.get("/api/items/{item_id}")
def get_item_details(item_id: str):
    """Obtiene los detalles de un producto específico por su ID."""
    if not db:
         raise HTTPException(
            status_code=503, detail="La base de datos de productos no está disponible."
        )

    for item in db:
        if item.get("id") == item_id:
            return item

    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/")
def read_root():
    """Endpoint raíz para verificar que la API está funcionando."""
    return {"status": "API is running"}
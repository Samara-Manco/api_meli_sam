# Registro de Prompts de GenAI

"Genera el código para una API con FastAPI en Python. El archivo principal debe ser src/main.py. Debe cargar los datos desde un archivo JSON ubicado en data/products.json. Crea un endpoint GET /api/items/{item_id} que busque un ítem por su id en la lista cargada. Si lo encuentra, debe devolver el objeto del ítem con un status 200. Si no lo encuentra, debe devolver un error HTTP 404 con un JSON {\"detail\": \"Item not found\"}. Incluye manejo de errores si el archivo JSON no existe."

Este archivo documenta los prompts utilizados durante el desarrollo para mejorar la eficiencia, siguiendo las directrices de la prueba técnica.

---
### Prompt 1: Generación de Código Base de la API

**Objetivo:** Crear la estructura inicial de la API con FastAPI, incluyendo la lógica de lectura de archivos y el manejo de errores.

**Prompt:**

Genera el código para una API básica con FastAPI en Python. El archivo principal debe ser src/main.py. Debe cargar los datos desde un archivo JSON ubicado en data/products.json. Crea un endpoint GET /api/items/{item_id} que busque un ítem por su id en la lista cargada. Si lo encuentra, debe devolver el objeto del ítem con un status 200. Si no lo encuentra, debe devolver un error HTTP 404 con un JSON {\"detail\": \"Item not found\"}. Incluye manejo de errores si el archivo JSON no existe y un endpoint raíz / que devuelva {\"status\": \"API is running\"}.

---
### Prompt 2: Generación de Pruebas Automatizadas

**Objetivo:** Crear la base para la suite de pruebas usando Pytest y el TestClient de FastAPI.

**Prompt:**

Genera una suite de pruebas para una aplicación FastAPI usando pytest y TestClient. El archivo de pruebas es tests/test_main.py. La app tiene un endpoint GET /api/items/{item_id}. Escribe tres pruebas: 

1. Una prueba de caso de éxito (test_read_item_success) que llame a un ID existente y verifique que el status sea 200 y el título sea el correcto.

2. Una prueba de caso de error (test_read_item_not_found) que llame a un ID inexistente y verifique que el status sea 404.

3. Una prueba para el endpoint raíz (test_root_endpoint) que verifique que el status sea 200.

---
### Prompt 3: Creación de Workflow de GitHub Actions

**Objetivo:** Generar la plantilla base para el archivo de Integración Continua.

**Prompt:**

Crea un workflow básico de GitHub Actions para un proyecto de Python. El workflow debe activarse en cada push a la rama 'main'. Debe tener un solo job que corra en ubuntu-latest. Los pasos deben ser:

1. Hacer checkout del código.

2. Configurar Python 3.11.

3. Instalar las dependencias desde un archivo requirements.txt.

4. Ejecutar las pruebas usando el comando pytest.
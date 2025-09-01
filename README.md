# api_meli_sam
# Prueba Técnica: API de Detalles de Producto (MercadoLibre)

![CI Pipeline](https://github.com/Samara-Manco/api_meli_sam/actions/workflows/apimeli-ci.yml/badge.svg)

Este repositorio contiene la solución a la prueba técnica para desarrollar una API de backend que proporciona los detalles de un producto, siguiendo las mejores prácticas de desarrollo y DevOps.

---
## ✨ Estrategia Técnica y Decisiones Arquitectónicas

La estrategia se centró en construir una solución robusta, portable y con calidad de código garantizada a través de la automatización.

### Pila Tecnológica
**Lenguaje:** Python 3.11
**Framework de API:** FastAPI
**Containerización:** Docker & Docker Compose
**Pruebas:** Pytest, Pytest-Cov, Pytest-HTML
**CI/CD:** GitHub Actions

### Arquitectura Container-First
La decisión arquitectónica principal fue desarrollar la aplicación de forma **nativa para contenedores** usando **Docker**. Esto garantiza:
1.  **Portabilidad:** La API se ejecuta de la misma manera en cualquier máquina.
2.  **Consistencia de Entorno:** Se eliminan los problemas de "en mi máquina sí funciona".
3.  **Facilidad de Despliegue:** Levantar todo el servicio se reduce a un solo comando.

### Calidad de Código Automatizada (CI/CD)
Se implementó un pipeline de Integración Continua con **GitHub Actions** que se activa en cada push. Este pipeline:
1.  **Instala las dependencias** en un entorno limpio.
2.  **Ejecuta la suite de pruebas automatizadas** con Pytest.
3.  **Calcula la cobertura de las pruebas (Code Coverage)**, asegurando que la lógica de negocio está validada (actualmente en **91%**).
4.  **Genera y publica un reporte de pruebas en HTML** como un artefacto descargable, ofreciendo una visualización profesional de los resultados.

---
## 🚀 Cómo Ejecutar el Proyecto

### Pre-requisitos
Git
Docker
Docker Compose

### Pasos
1.  **Clonar el repositorio:**
   
bash
    git clone [https://github.com/Samara-Manco/api_meli_sam.git](https://github.com/Samara-Manco/api_meli_sam.git)
   
2.  **Navegar a la carpeta del proyecto:**
   
bash
    cd api_meli_sam
   
3.  **Levantar los servicios con Docker Compose:**
   
bash
    docker-compose up --build
   
La API estará disponible en http://localhost:8000.

---
## ⚙️ Uso de la API

**Documentación Interactiva (Swagger UI):**
    Una vez levantada la API, la documentación autogenerada e interactiva está disponible en:
    [**http://localhost:8000/docs**](http://localhost:8000/docs)

**Endpoint de Detalles de Producto:** GET /api/items/{item_id}

    **Ejemplo con cURL:**
   
bash
    curl http://localhost:8000/api/items/MLA123456
   

---
## 🤖 Integración con GenAI y Herramientas Modernas

Se utilizaron herramientas de IA Generativa para mejorar la eficiencia en varias etapas del desarrollo, como se detalla en el archivo prompts.md. Los usos principales fueron:
**Generación de código base (Boilerplate):** Para crear la estructura inicial de la API con FastAPI.
**Creación de pruebas unitarias:** Para generar los casos de prueba base.
**Resolución de dudas:** Para entender errores específicos y generar configuraciones como el Dockerfile inicial.
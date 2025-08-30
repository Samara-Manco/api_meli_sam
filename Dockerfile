# Fase 1: Usar una imagen oficial de Python como base
FROM python:3.11-slim as base

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Prevenir que Python escriba archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevenir que Python bufferice stdout y stderr
ENV PYTHONUNBUFFERED 1

# Copiar solo el archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY ./src ./src
COPY ./data ./data

# Exponer el puerto en el que correrá la app
EXPOSE 8000

# Comando para correr la aplicación cuando el contenedor inicie
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
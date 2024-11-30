FROM python:3.11-slim

# Instalación de paquetes para dependencias del proyecto
RUN apt-get update && apt-get install -y \
  pkg-config \
  gcc \
  pkg-config \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/

# Actualiza pip a la última versión
RUN pip install --no-cache-dir --upgrade pip

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

RUN pip install gunicorn

# Copia de ficheros a contenedor
COPY api_backend/ /app/

# Directorio /app/logs y creación de gunicorn_error.log
RUN mkdir -p /app/logs && touch /app/logs/gunicorn_error.log

# Copia el entrypoint.sh al directorio /app en el contenedor
COPY entrypoint.sh /entrypoint.sh

RUN ["chmod", "+x", "/entrypoint.sh"]

# Ejecutar la aplicación Flask
ENTRYPOINT ["/entrypoint.sh"]

# Puerto en el que corre la aplicación Flask
EXPOSE 5000

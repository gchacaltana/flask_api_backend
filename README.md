# Flask API Backend

Repositorio oficial del proyecto Flask API Backend.

## Overview

Este proyecto consiste en una aplicación Restful API para administrar la información
de personajes de películas.

## Tech Stack

* Backend: Python 3.12.1 - Flask Framework 3.1.0.
* Database: SQLite3
* Web Proxy: Nginx v1.18.0
* Docker: 26.1.3
* Docker-Compose: 1.29.2 

## Requisitos

* Python ^3.12

## Dependencias

```bash
Flask==3.1.0
Flask-JWT-Extended==4.7.1
flask-marshmallow==1.2.1
Flask-SQLAlchemy==3.1.1
marshmallow==3.23.1
marshmallow-sqlalchemy==1.1.0
PyJWT==2.10.1
python-dotenv==1.0.1
SQLAlchemy==2.0.36
Werkzeug==3.1.3
```

## Documentación API

* URL: https://app.swaggerhub.com/apis/gchacaltanab/flask-api/1.0.0

## Ejecución de Pruebas

* Ejecutar pruebas unitarias

```bash
pytest api_backend/tests/unit/
```

* Ejecutar pruebas de integración

```bash
pytest api_backend/tests/integration/
```

## Desplegar en entorno desarrollo

1. Clonar repositorio e ingresar a proyecto.
2. Crear y activar entorno virtual

```bash
py -m venv venv
source venv/bin/activate # Linux
source venv/Scripts/activate # windows
```

3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

4. Opcional: Crear una cuenta de usuario para login y obtener JWT.

```bash
py api_backend/scripts/create_user.py
```

5. Crear archivo .env en directorio raíz del proyecto con siguiente estructura

```bash
APP_ENVIRONMENT="development"
DEBUG=true
PORT=5000
APP_NAME="Flask API"
APP_VERSION="1.0.0"
APP_HOST="localhost"
JWT_SECRET_KEY="<secret>"
JWT_EXPIRES_MIN=30
DB_URI=sqlite:///db.sqlite3
PAGINATE_PER_PAGE=5
```

6. Ejecutar aplicación en local

```bash
# Linux
./run_dev.sh

# Windows
sh run_dev.sh
```

## Deploy Automatico - Integración con Github Actions

* Al realizar un commit o PR en la rama master, se activa un workflow de GitHub Actions que construye, publica y despliega automáticamente la imagen Docker de la aplicación backend.

## Deploy Manual Producción

* Generar y publicar imagen docker (Local)

```bash
docker build . -t <dockerhub_account>/flask_api:latest && docker push <dockerhub_account>/flask_api:latest
```

* Levantar aplicación desde el docker-compose.yml (Producción)

```bash
docker-compose up -d
```
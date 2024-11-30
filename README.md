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

5. Desplegar aplicación

```bash
# Linux
./run_dev.sh

# Windows
sh run_dev.sh
```

## Deploy Automatico - Integración con Github Actions

* Al hacer un commit en la rama "master" se activa el workflow de Github Actions, se construye y publican las imagenes docker de la aplicación backend.


# Deploy Manual Producción

* Generar imagen docker asignado una nueva versión (Local)

```bash
docker build . -t ghcr.io/<github_account>/flask_api:<app_version> && docker push ghcr.io/gchacaltana/flask_api:<app_version>
```

* Ingresar a servidor, cambiar versión de imagen en docker-compose.yml y levantar aplicación.

```bash
docker-compose up -d
```
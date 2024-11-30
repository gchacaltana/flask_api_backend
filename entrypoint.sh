#!/bin/bash

# Carga las variables de entorno
if [ -f .env ]; then
  export $(cat .env | xargs)
fi

# Variable GUNICORN para ejecutar aplicación en producción
if [ "$GUNICORN" = "true" ]; then
    echo "Iniciando la aplicación con Gunicorn..."
    gunicorn entrypoint:app \
    --error-logfile=/app/logs/gunicorn_error.log \
    --workers=3 \
    --log-level=debug \
    --preload \
    --bind=0.0.0.0:5000
fi
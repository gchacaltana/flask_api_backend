# Script Bash para levantar aplicación en entorno local

# Paso 1: Activar entorno virtual.
# source venv/Script/activate

# Paso 2: Seteamos las variables de entorno
source ./.env

# Paso 3: Levantar aplicación
py api_backend/entrypoint.py
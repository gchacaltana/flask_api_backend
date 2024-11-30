"""
app/entrypoint.py
Punto de entrada para ejecutar aplicación
"""
import os
from dotenv import load_dotenv
from app import create_app
from app.config.settings import ApplicationConfig
load_dotenv()

config_name = os.getenv('APP_ENVIRONMENT', 'development')

app = create_app(config_name)
app.config.from_object(ApplicationConfig)

if __name__ == '__main__':
    app.run(
        debug=ApplicationConfig.DEBUG,
        host=ApplicationConfig.HOST, 
        port=ApplicationConfig.PORT
    )

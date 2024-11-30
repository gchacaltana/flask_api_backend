"""
app/config/settings.py
Configuration for the Flask app.
"""
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class SQLAlchemyConfig:
    """
    Configuración para el SQLAlchemy.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class JWTConfig:
    """
    Configuración para el JWT.
    """
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=int(os.getenv("JWT_EXPIRES_MIN", "30")))


class Setting(
    SQLAlchemyConfig, JWTConfig
):
    """
    Configuración para la aplicación.
    """
    NAME = os.getenv("APP_NAME")
    HOST = os.getenv("APP_HOST")
    PORT = os.getenv("APP_PORT")
    DEBUG = os.getenv("APP_DEBUG", "false").lower() == "true"
    APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT")
    SECRET_KEY = os.getenv("SECRET_KEY")
    PAGINATE_PER_PAGE = int(os.getenv("PAGINATE_PER_PAGE", "10"))

"""
app/__init__.py
"""
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import settings

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    """
    Crea una instancia de la aplicación de Flask.
    """
    app = Flask(__name__)
    jwt = JWTManager(app)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLAlchemyConfig.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialización de extensiones
    db.init_app(app)
    ma.init_app(app)

     # Registrar rutas (blueprints)
    from app.routes.home_route import home_bp
    from app.routes.auth_route import auth_bp
    from app.routes.character_route import character_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(character_bp)

    # Inicialización de la base de datos
    with app.app_context():
        db.create_all()

    return app

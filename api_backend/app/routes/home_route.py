"""
app/routes/home_route.py
"""
from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def home():
    """
    Home Endpoint de la API
    """
    return jsonify({'message': 'Bienvenido a la API de personajes'})


@home_bp.errorhandler(404)
def not_found(error):
    """
    Endpoint para manejar errores 404
    """
    response = {
        "error": "Not Found",
        "message": "El recurso solicitado no fue encontrado"
    }
    return jsonify(response), 404

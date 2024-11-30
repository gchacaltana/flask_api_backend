"""
app/routes/character_route.py
Rutas para manejar las peticiones de personajes.
"""
from flask import Blueprint, request, jsonify
from app.config.logger_config import logger
from marshmallow import ValidationError
from app.exceptions.api_exception import APIException
from app.exceptions.resource_not_found_exception import ResourceNotFoundException
from flask_jwt_extended import jwt_required
from app.config.settings import ApplicationConfig
from app.services.character_service import (
    get_characters_service, add_character_service, validate_character_exists,
    delete_character_service
)

character_bp = Blueprint('character', __name__, url_prefix='/character')


@character_bp.route('/getAll', methods=['GET'])
def get_characters_route():
    """
    Endpoint para obtener todos los personajes
    Returns:
        List: Lista de personajes
    Raises:
        APIException: Error interno
    """
    try:
        logger.info("Acceso al endpoint '/character/getAll' - IP: %s",
                    request.remote_addr)
        # Parametros de paginación
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get(
            'per_page', ApplicationConfig.PAGINATE_PER_PAGE, type=int)
        return jsonify(get_characters_service(page, per_page)), 200
    except APIException as err:
        return jsonify({"errors": str(err)}), 500


@character_bp.route('/add', methods=['POST'])
@jwt_required()
def add_character_route():
    """
    Endpoint para crear un nuevo personaje
    Returns:
        JSON: Personaje creado
    Raises:
        ValidationError: Error de validación
        APIException: Error interno
    """
    try:
        logger.info("Acceso al endpoint '/character/add' - IP: %s",request.remote_addr)
        logger.debug("Petición recibida - %s", request.get_json())
        return jsonify(add_character_service(request.get_json())), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except APIException as err:
        return jsonify({"errors": str(err)}), 500


@character_bp.route('/get/<int:character_id>', methods=['GET'])
def get_character_route(character_id: int):
    """
    Endpoint para obtener un personaje por su ID
    """
    try:
        logger.info("Acceso al endpoint '/character/get/%s' - IP: %s",character_id, request.remote_addr)
        return jsonify(validate_character_exists(character_id)), 200
    except ResourceNotFoundException as err:
        return jsonify({"errors": str(err)}), 400
    except APIException as err:
        return jsonify({"errors": str(err)}), 500


@character_bp.route('/delete/<int:character_id>', methods=['DELETE'])
@jwt_required()
def delete_character_route(character_id: int):
    """
    Endpoint para eliminar un personaje por su ID
    Returns:
        JSON: Mensaje de confirmación
    """
    try:
        logger.info("Acceso al endpoint '/character/delete/%s' - IP: %s",character_id, request.remote_addr)
        return jsonify(delete_character_service(character_id)), 200
    except ResourceNotFoundException as err:
        return jsonify({"errors": str(err)}), 400
    except APIException as err:
        return jsonify({"errors": str(err)}), 500

"""
app/routes/auth_route.py
"""
from flask import Blueprint, jsonify, request
from app.config.logger_config import logger
from marshmallow import ValidationError
from app.exceptions.api_exception import APIException
from app.services.auth_service import auth_service
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login_route():
    """
    Endpoint de autenticación del usuario para generar token JWT.
    """
    try:
        logger.info("Acceso al endpoint '/login' - IP: %s", request.remote_addr)
        logger.debug("Petición recibida - %s", request.get_json())
        data = request.get_json()
        access_token = auth_service(data)
        if access_token:
            logger.info("Usuario autenticado - Access Token: %s", access_token)
            return jsonify(access_token=access_token), 200
        logger.info("Credenciales incorrectas - IP: %s", request.remote_addr)
        return jsonify(message="Credenciales incorrectas"), 401
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except APIException as err:
        return jsonify({"errors": str(err)}), 500
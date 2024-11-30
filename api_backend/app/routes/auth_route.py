"""
app/routes/auth_route.py
"""
from flask import Blueprint, jsonify, request
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
        data = request.get_json()
        access_token = auth_service(data)
        if access_token:
            return jsonify(access_token=access_token), 200
        return jsonify(message="Invalid credentials"), 401
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except APIException as err:
        return jsonify({"errors": str(err)}), 500
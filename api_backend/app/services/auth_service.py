"""
app/services/auth_service.py
"""

from app.schemas.user_schema import UserSchema
from flask_jwt_extended import create_access_token
from app.repositories.user_repository import get_user_by_username


def auth_service(data: dict):
    """
    Función para autenticar un usuario y generar un token JWT (access token)
    """
    user_schema = UserSchema()
    validated_data = user_schema.load(data)
    user = get_user_by_username(validated_data.username)
    if user and user.check_password(data.get('password')):
        return create_access_token(identity=validated_data.username)
    return None

"""
app/schemas/character.py
"""
from marshmallow import fields, validate
from app.models.user import User
from app import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    Esquema de serialización/deserialización de Usuario
    """

    username = fields.String(required=True, validate=[validate.Length(min=3, max=50)], error_messages={
        "required": "El nombre de usuario es requerido",
        "invalid": "El nombre de usuario es inválido",
        "length": "El nombre debe tener entre 3 y 50 caracteres"
    })

    password = fields.String(required=True, validate=[validate.Length(min=8, max=20)], error_messages={
        "required": "La contraseña es requerida",
        "invalid": "La contraseña es inválida",
        "length": "La contraseña debe tener entre 8 y 20 caracteres"
    })

    class Meta:
        """
        Meta
        """
        model = User
        load_instance = True
        fields = (
            "id", "username", "password"
        )
        
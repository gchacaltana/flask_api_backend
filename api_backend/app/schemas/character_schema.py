"""
app/schemas/character.py
"""
from marshmallow import fields, validate
from app.models.character import Character
from app import ma


class CharacterSchema(ma.SQLAlchemyAutoSchema):
    """
    Esquema de serialización/deserialización de Personaje (Character)
    """

    name = fields.String(required=True, validate=[validate.Length(min=3, max=80)], error_messages={
        "required": "El nombre es requerido",
        "invalid": "El nombre es inválido",
        "length": "El nombre debe tener entre 3 y 80 caracteres"
    })
    height = fields.Integer(required=True, validate=[validate.Range(min=50, max=250)], error_messages={
        "required": "La altura es requerida",
        "invalid": "La altura es inválida, debe ser un número entero",
        "range": "La altura debe estar entre 50 y 250"
    })
    mass = fields.Integer(required=True, validate=[validate.Range(min=10, max=200)], error_messages={
        "required": "El peso es requerido",
        "invalid": "El peso es inválido, debe ser un número entero",
        "range": "El peso debe estar entre 10 y 200"
    })
    hair_color = fields.String(required=True, validate=[validate.Length(min=3, max=30)], error_messages={
        "required": "El color de cabello es requerido",
        "invalid": "El color de cabello es inválido",
        "length": "El color de cabello debe tener entre 3 y 30 caracteres"
    })
    skin_color = fields.String(required=True, validate=[validate.Length(min=3, max=30)], error_messages={
        "required": "El color de piel es requerido",
        "invalid": "El color de piel es inválido",
        "length": "El color de piel debe tener entre 3 y 30 caracteres"
    })
    eye_color = fields.String(required=True, validate=[validate.Length(min=3, max=30)], error_messages={
        "required": "El color de ojos es requerido",
        "invalid": "El color de ojos es inválido",
        "length": "El color de ojos debe tener entre 3 y 30 caracteres"
    })
    birth_year = fields.Integer(required=True, validate=[validate.Range(min=1900, max=2024)], error_messages={
        "required": "El año de nacimiento es requerido",
        "invalid": "El año de nacimiento es inválido, debe ser un número entero",
        "range": "El año de nacimiento debe estar entre 1900 y 2024",
        "greater_than": "El año de nacimiento debe ser mayor a 1900",
        "less_than": "El año de nacimiento debe ser menor a 2024"
    })

    class Meta:
        """
        Meta
        """
        model = Character
        load_instance = True
        fields = (
            "id", "name", "height", "mass", "hair_color", "skin_color",
            "eye_color", "birth_year"
        )

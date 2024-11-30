"""
app/repositories/character_repository.py
Funciones para manejar el acceso a la base de datos para la entidad Character
"""
from app.schemas.character_schema import CharacterSchema
from app.models.character import Character
from app import db

def fecth_characters(page:int, per_page:int):
    """
    Obtener personajes de la base de datos con paginación
    """
    characters = Character.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    return characters

def save_character(data):
    """
    Guardar nuevo personaje en base de datos
    """
    character_schema = CharacterSchema()
    new_character = character_schema.load(data)
    db.session.add(new_character)
    db.session.commit()
    return character_schema.dump(new_character)

def get_character_by_id(character_id: int):
    """
    Obtener personaje por ID
    """
    return Character.query.get(character_id)

def delete_character(character):
    """
    Eliminar personaje por ID
    """
    db.session.delete(character)
    db.session.commit()
    return True

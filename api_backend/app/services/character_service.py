"""
app/services/character_service.py
Funciones para manejar la lógica de negocio de personajes.
"""
from app.schemas.character_schema import CharacterSchema
from app.exceptions.resource_not_found_exception import ResourceNotFoundException
from app.repositories.character_repository import (
    fecth_characters, save_character,
    get_character_by_id,
    delete_character
)


def get_characters_service(page: int, per_page: int):
    """
    Devuelve paginacion de personajes
    """
    # Consultar personajes con paginación
    characters = fecth_characters(page, per_page)
    character_schema = CharacterSchema(many=True)
    payload = character_schema.dump(characters.items)
    response = {
        "total": characters.total,
        "pages": characters.pages,
        "current_page": characters.page,
        "per_page": characters.per_page,
        "data": payload
    }
    return response


def add_character_service(data:dict):
    """
    Service para crear nuevo personaje en base de datos
    """
    return save_character(data)


def validate_character_exists(character_id: int):
    """
    Service para validar si un personaje existe
    """
    character = get_character_by_id(character_id)
    if not character:
        raise ResourceNotFoundException(f'Personaje con ID {character_id} no existe')
    character_schema = CharacterSchema()
    return character_schema.dump(character)

def delete_character_service(character_id: int):
    """
    Service para eliminar personaje por ID
    """
    character = get_character_by_id(character_id)
    if not character:
        raise ResourceNotFoundException(f'Personaje con ID {character_id} no existe')
    delete_character(character)
    return {'message': 'Personaje eliminado'}

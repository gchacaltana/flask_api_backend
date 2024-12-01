"""
tests/test_character.py
"""
import pytest
from app import create_app, db
from app.repositories.character_repository import save_character


@pytest.fixture
def client():
    """
    Fixture para el cliente de pruebas
    """
    app = create_app('testing')
    with app.app_context():
        yield app.test_client()
        db.drop_all()


# Test para verificar si un personaje se guarda correctamente en la base de datos
def test_create_character(client):
    """
    Prueba para crear un personaje
    """
    character_data = {
        'name': 'Anakin Skywalker',
        'height': 180,
        'mass': 80,
        'hair_color': 'black',
        'skin_color': 'fair',
        'eye_color': 'brown',
        'birth_year': 1989
    }
    # Crear el personaje usando la función save_character
    new_character = save_character(character_data)
    assert new_character['name'] == character_data['name']
    assert new_character['height'] == character_data['height']
    assert new_character['mass'] == character_data['mass']
    assert new_character['hair_color'] == character_data['hair_color']
    assert new_character['birth_year'] == character_data['birth_year']

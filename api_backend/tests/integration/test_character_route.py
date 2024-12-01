"""
tests/integration/test_character_route.py
"""
import pytest
from app import create_app, db
from flask.testing import FlaskClient
from app.repositories.character_repository import save_character

@pytest.fixture
def client() -> FlaskClient:
    """
    Fixture para el cliente de pruebas
    """
    app = create_app('testing')
    with app.app_context():
        yield app.test_client()
        db.drop_all()
    return app.test_client()


def test_get_all_characters(client: FlaskClient):
    """
    Prueba para obtener todos los personajes
    """
    response = client.get("/character/getAll")
    assert response.status_code == 200
    assert 'current_page' in response.json
    assert 'pages' in response.json
    assert 'data' in response.json
    assert 'per_page' in response.json
    assert 'total' in response.json
    assert len(response.json['data']) == 0
    assert response.json['per_page'] == 5
    assert response.json['current_page'] == 1

def test_get_character_by_id_not_found(client: FlaskClient):
    """
    Prueba para obtener un personaje por ID que no existe
    """
    response = client.get("/character/get/1")
    assert response.status_code == 400
    assert 'errors' in response.json

def test_get_character_by_id_success(client: FlaskClient):
    """
    Prueba para obtener un personaje por ID
    """
    save_character({
        'name': 'Anakin Skywalker',
        'height': 180,
        'mass': 80,
        'hair_color': 'black',
        'skin_color': 'fair',
        'eye_color': 'brown',
        'birth_year': 1989
    })
    response = client.get("/character/get/1")
    assert response.status_code == 200
    assert 'birth_year' in response.json
    assert 'eye_color' in response.json
    assert 'hair_color' in response.json
    assert 'height' in response.json
    assert 'mass' in response.json
    assert 'name' in response.json
    assert response.json['name'] == 'Anakin Skywalker'
    assert response.json['height'] == 180
    assert response.json['mass'] == 80
    assert response.json['hair_color'] == 'black'
    assert response.json['birth_year'] == 1989

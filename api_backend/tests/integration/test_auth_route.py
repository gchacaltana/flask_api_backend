"""
tests/integration/test_auth_route.py
"""
import pytest
from app import create_app, db
from flask.testing import FlaskClient
from app.repositories.user_repository import get_user_by_username, save_user

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

def test_login_success(client: FlaskClient):
    """
    Prueba que verifica un login exitoso y la generación del access token
    """
    # Creamos un usuario en la base de datos para la prueba
    user_data = {"username": "usertest00", "password": "usertest12345"}
    # Verificar que el usuario no exista
    user = get_user_by_username(user_data['username'])
    if user is not None:
        db.session.delete(user)
        db.session.commit()
    # Crear el usuario usando la función save_user
    new_user = save_user(user_data['username'], user_data['password'])
    if new_user is not None:
        # Intentar iniciar sesión con las credenciales creadas
        login_payload = {"username": user_data["username"], "password": user_data["password"]}
        response = client.post("/login", json=login_payload)

        # Verificar que el endpoint devuelve el token correctamente
        assert response.status_code == 200
        data = response.get_json()
        assert "access_token" in data
        assert isinstance(data["access_token"], str)

def test_login_failure_invalid_credentials(client: FlaskClient):
    """
    Prueba que verifica el fallo al intentar login con credenciales incorrectas
    """
    # Intentar iniciar sesión con credenciales incorrectas
    login_payload = {"username": "invaliduser", "password": "usertest12345"}
    response = client.post("/login", json=login_payload)

    # Verificar que el endpoint devuelve un error
    assert response.status_code == 401
    data = response.get_json()
    assert "message" in data
    assert data["message"] == "Credenciales incorrectas"

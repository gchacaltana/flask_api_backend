import pytest
from app import create_app, db
from app.models.user import User
from app.repositories.user_repository import save_user, get_user_by_username

@pytest.fixture
def client():
    """
    Fixture para el cliente de pruebas
    """
    app = create_app('testing')
    with app.app_context():
        yield app.test_client()
        db.drop_all()

# Test para verificar si un usuario se guarda correctamente en la base de datos
def test_create_user(client):
    """
    Prueba para crear un usuario
    """
    user_data = {
        'username': 'newuser',
        'password': 'securepassword'
    }
    # Verificar que el usuario no exista
    user = get_user_by_username(user_data['username'])
    if user is not None:
        db.session.delete(user)
        db.session.commit()
    # Crear el usuario usando la función save_user
    new_user = save_user(user_data['username'], user_data['password'])
    assert new_user.id is not None
    assert new_user.username == user_data['username']
    assert new_user.check_password(user_data['password'])
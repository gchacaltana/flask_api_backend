"""
app/repositories/user_repository.py
Funciones para manejar el acceso a la base de datos para la entidad User
"""
from app.models.user import User
from app import db


def get_user_by_username(username: str):
    """
    Función para obtener un usuario por nombre de usuario
    """
    return User.query.filter_by(username=username).first()


def save_user(username: str, password: str):
    """
    Guardar nuevo usuario en base de datos
    """
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

"""
scripts/create_admin_user.py
script para insertar un usuario admin en la base de datos.
"""
import sys
import os
import re

# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import create_app
from app.repositories.user_repository import (get_user_by_username, save_user)

app = create_app()


def create_admin_user(username:str, password:str):
    """
    Función para insertar un usuario admin en la base de datos.
    """
    with app.app_context():
        user = get_user_by_username(username)
        if user:
            print(f"El usuario con username {username} ya existe.")
            return

        # Registrar usuario
        new_user = save_user(username, password)
        print(f"Usuario {new_user.username} creado exitosamente.")


def clean_input_username(username: str):
    """
    Función para limpiar y validar el nombre de usuario.
    """
    username = username.strip()
    if not username:
        raise ValueError("El nombre de usuario no puede estar vacío.")

    # Limitar a caracteres alfanuméricos (letras y números)
    if not re.match("^[a-zA-Z0-9_]+$", username):
        raise ValueError(
            "El nombre de usuario solo puede contener letras, números y guiones bajos.")

    return username.lower()


def clean_input_password(password: str):
    """
    Función para limpiar y validar la contraseña.
    """
    password = password.strip()

    if not password:
        raise ValueError("La contraseña no puede estar vacía.")

    # Validar contraseña a 8 caracteres como mínimo
    if len(password) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")

    return password


if __name__ == "__main__":
    try:
        # Solicitar nombre de usuario y contraseña
        username = clean_input_username(input("Ingresa el nombre de usuario: "))
        password = clean_input_password(input("Ingresa una contraseña: "))

        # Insertar usuario
        create_admin_user(username, password)
    except ValueError as e:
        print(f"Error: {e}")

"""
app/models/user.py
"""
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """
    Modelo de usuario
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.username}>"

    def set_password(self, password: str):
        """
        Método para establecer la contraseña encriptada
        """
        self.password = generate_password_hash(password)

    def check_password(self, password: str):
        """
        Método para verificar la contraseña
        """
        return check_password_hash(self.password, password)

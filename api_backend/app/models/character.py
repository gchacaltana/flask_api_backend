"""
app/models/character.py
"""
from app import db


class Character(db.Model):
    """
    Modelo Personaje (Character)
    """
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(30), nullable=False)
    skin_color = db.Column(db.String(30), nullable=False)
    eye_color = db.Column(db.String(30), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, height:int, mass:int, hair_color:str, skin_color:str, eye_color:str, birth_year:int):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year

    def __repr__(self):
        return f'<Personaje {self.name}>'

    def to_dict(self):
        """
        Retorna un diccionario con los datos del personaje
        """
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'eye_color': self.eye_color,
            'birth_year': self.birth_year
        }

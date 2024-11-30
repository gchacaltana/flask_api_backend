"""
app/exceptions/APIException.py
"""


class APIException(Exception):
    """Excepción personalizada para la API"""

    def __init__(self, message, status_code=500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        """Convierte la excepción en un diccionario JSON"""
        return {"error": self.message, "status_code": self.status_code}

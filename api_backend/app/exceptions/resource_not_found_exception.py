"""
app/exceptions/resource_not_found_exception.py
"""


class ResourceNotFoundException(Exception):
    """
    Excepción para recursos no encontrados.
    """

    def __init__(self, message="Recurso no encontrado"):
        self.message = message
        super().__init__(self.message)

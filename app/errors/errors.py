class CustomException(Exception):
    """Base class for custom exceptions"""
    pass

class UserNotFoundError(CustomException):
    """Raised when an attempt to find a user that does not exist is made"""
    def __init__(self, message="No se encontró el usuario", param=None):
        self.message = message
        self.param = param
        if param:
            self.message += f": '{param}'"
        super().__init__(self.message)

class FountainNotFoundError(CustomException):
    """Raised when an attempt to find a fountain that does not exist is made"""
    def __init__(self, message="No se encontró la fuente", param=None):
        self.message = message
        self.param = param
        if param:
            self.message += f": '{param}'"
        super().__init__(self.message)

class FountainAlreadyExistError(CustomException):
    """Raised when an attempt to create a fountain that already exists is made"""
    def __init__(self, message="La fuente ya existe"):
        self.message = message
        super().__init__(self.message)
        
class WarningNotFoundError(CustomException):
    """Raised when an attempt to find a warning that does not exist is made"""
    def __init__(self, message="No se encontró la advertencia", param=None):
        self.message = message
        self.param = param
        if param:
            self.message += f": '{param}'"
        super().__init__(self.message)
    
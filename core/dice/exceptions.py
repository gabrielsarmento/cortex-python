class DieException(Exception):
    """Generic Die Exception"""
    pass


class DieFacesValueException(DieException):
    """Number of faces not allowed for a die"""
    pass


class DieOperationException(DieException):
    """Die Operation not allowed"""
    pass

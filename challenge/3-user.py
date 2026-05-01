def is_valid_password(self, pwd):
    """Validate password"""
    if pwd is None:
        return False
    return self.__password == pwd

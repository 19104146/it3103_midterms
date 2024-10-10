class UserConflictException(Exception):
    def __init__(self, message: str = "User already exists"):
        self.message = message
        super().__init__(self.message)


class UserNotFoundException(Exception):
    def __init__(self, message: str = "User not found"):
        self.message = message
        super().__init__(self.message)

class ProductConflictException(Exception):
    def __init__(self, message: str = "Product already exists"):
        self.message = message
        super().__init__(self.message)


class ProductNotFoundException(Exception):
    def __init__(self, message: str = "Product not found"):
        self.message = message
        super().__init__(self.message)

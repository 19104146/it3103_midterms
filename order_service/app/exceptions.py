class OrderNotFoundException(Exception):
    def __init__(self, message: str = "Order not found"):
        self.message = message
        super().__init__(self.message)

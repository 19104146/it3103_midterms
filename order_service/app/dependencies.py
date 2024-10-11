from functools import lru_cache

from app.services import OrderService


@lru_cache
def get_order_service():
    return OrderService()

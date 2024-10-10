from functools import lru_cache

from app.services.product import ProductService


@lru_cache
def get_product_service():
    return ProductService()

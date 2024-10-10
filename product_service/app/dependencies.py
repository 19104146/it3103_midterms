from functools import lru_cache

from app.services.product_service import ProductService


@lru_cache
def get_product_service():
    return ProductService()

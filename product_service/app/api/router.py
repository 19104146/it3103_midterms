from fastapi import APIRouter

from app.api.products import router as products_router

router = APIRouter()

router.include_router(products_router, prefix="/products", tags=["products"])

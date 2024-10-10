from fastapi import FastAPI

from app.routers.product import router as product_router
from app.settings import settings

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(product_router, prefix="/products", tags=["products"])

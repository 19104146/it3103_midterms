from fastapi import FastAPI

from app.routers import router
from app.settings import settings

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(router, prefix="/products", tags=["products"])

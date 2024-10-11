from fastapi import FastAPI

from app.config import config
from app.routers.admin import router as admin_router
from app.routers.protected import router as protected_router
from app.routers.public import router as public_router

app = FastAPI(title=config.APP_NAME, version=config.APP_VERSION)

app.include_router(public_router)
app.include_router(protected_router)
app.include_router(admin_router)

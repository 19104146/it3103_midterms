from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.user import router as user_router
from app.settings import settings

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(auth_router)
app.include_router(user_router, prefix="/users", tags=["users"])

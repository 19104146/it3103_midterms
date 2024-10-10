from functools import lru_cache

from app.dependencies.user import get_user_service
from app.services.auth import AuthService


@lru_cache
def get_auth_service():
    return AuthService(get_user_service())

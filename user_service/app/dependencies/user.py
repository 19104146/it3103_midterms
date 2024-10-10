from functools import lru_cache

from app.services.user import UserService


@lru_cache
def get_user_service():
    return UserService()

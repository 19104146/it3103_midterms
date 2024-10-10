from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext

from app.exceptions.auth import AuthUnauthorizedException
from app.exceptions.user import UserNotFoundException
from app.schemas.user import UserRead
from app.services.user import UserService
from app.settings import settings


class AuthService:
    def __init__(self, user_service: UserService):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.user_service = user_service

    def verify_password(self, password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def get_user(self, username: str) -> UserRead:
        existing_user = next(
            (user for user in self.user_service.users if user.username == username),
            None,
        )
        if not existing_user:
            raise UserNotFoundException()
        return existing_user

    def authenticate_user(self, username: str, password: str) -> UserRead:
        existing_user = self.get_user(username)
        if not self.verify_password(password, existing_user.password):
            raise AuthUnauthorizedException()
        return existing_user

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        to_encode.update(
            {"exp": datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_EXPIRY)}
        )
        encoded_jwt = jwt.encode(
            to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM
        )
        return encoded_jwt

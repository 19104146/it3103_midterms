from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies.auth import get_auth_service
from app.exceptions.auth import AuthUnauthorizedException
from app.exceptions.user import UserConflictException, UserNotFoundException
from app.schemas.user import UserWrite
from app.services.auth import AuthService

router = APIRouter()


@router.post("/login")
def login(
    user: UserWrite, auth_service: AuthService = Depends(get_auth_service)
) -> str:
    try:
        existing_user = auth_service.authenticate_user(user.username, user.password)
        return auth_service.create_access_token(
            {
                "id": existing_user.id,
                "username": existing_user.username,
                "role": existing_user.role,
            }
        )
    except AuthUnauthorizedException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except UserNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/register")
def register(
    user: UserWrite, auth_service: AuthService = Depends(get_auth_service)
) -> None:
    try:
        hashed_password = auth_service.get_password_hash(user.password)
        auth_service.user_service.create_user(
            UserWrite(username=user.username, password=hashed_password)
        )
    except UserConflictException:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    except UserNotFoundException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_404_NOT_FOUND)

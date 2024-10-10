from fastapi import APIRouter, Depends, HTTPException, status
from typing_extensions import List

from app.dependencies.user import get_user_service
from app.exceptions.user import UserConflictException, UserNotFoundException
from app.schemas.user import UserRead, UserWrite
from app.services.user import UserService

router = APIRouter()


@router.get("/", response_model=List[UserRead])
def list_users(user_service: UserService = Depends(get_user_service)):
    return user_service.list_users()


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(
    user: UserWrite,
    user_service: UserService = Depends(get_user_service),
) -> UserRead:
    try:
        return user_service.create_user(user)
    except UserConflictException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_409_CONFLICT)


@router.get("/{user_id}", response_model=UserRead)
def read_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
) -> UserRead:
    try:
        return user_service.read_user(user_id)
    except UserNotFoundException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{user_id}", response_model=UserRead)
def update_user(
    user_id: int,
    user: UserWrite,
    user_service: UserService = Depends(get_user_service),
) -> UserRead:
    try:
        return user_service.update_user(user_id, user)
    except UserNotFoundException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_404_NOT_FOUND)
    except UserConflictException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_409_CONFLICT)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
) -> None:
    try:
        user_service.delete_user(user_id)
    except UserNotFoundException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_404_NOT_FOUND)

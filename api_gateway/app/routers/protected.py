from fastapi import APIRouter, Depends, HTTPException, Request
from starlette import status
from typing_extensions import Annotated, Any, Dict

from app.auth import get_current_user
from app.config import config
from app.proxy import forward_request

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.api_route("/users/{user_id}", methods=["GET", "PUT", "DELETE"])
async def rud_user(
    request: Request,
    user_id: int,
    current_user: Annotated[Dict[str, Any], Depends(get_current_user)],
):
    if current_user["id"] != user_id:
        raise HTTPException(
            detail="You don't have permission to access this user's information",
            status_code=status.HTTP_403_FORBIDDEN,
        )

    return await forward_request(request, f"{config.USER_SERVICE_URL}/users/{user_id}")

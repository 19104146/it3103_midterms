from fastapi import APIRouter, Depends, HTTPException, Request
from starlette import status
from typing_extensions import Annotated, Any, Dict

from app.auth import get_current_user
from app.config import config
from app.proxy import forward_request

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.post("/products")
async def create_products(
    request: Request,
    current_user: Annotated[Dict[str, Any], Depends(get_current_user)],
):
    if current_user["role"] != "ADMIN":
        raise HTTPException(
            detail="You don't have permission to access this service",
            status_code=status.HTTP_403_FORBIDDEN,
        )

    return await forward_request(request, f"{config.PRODUCT_SERVICE_URL}/products")


@router.api_route("/products/{product_id}", methods=["PUT", "DELETE"])
async def ud_product(
    request: Request,
    product_id: int,
    current_user: Annotated[Dict[str, Any], Depends(get_current_user)],
):
    if current_user["role"] != "ADMIN":
        raise HTTPException(
            detail="You don't have permission to access this service",
            status_code=status.HTTP_403_FORBIDDEN,
        )

    return await forward_request(
        request,
        f"{config.PRODUCT_SERVICE_URL}/products/{product_id}",
    )


@router.api_route("/users", methods=["GET", "POST"])
async def cr_users(
    request: Request,
    current_user: Annotated[Dict[str, Any], Depends(get_current_user)],
):
    if current_user["role"] != "ADMIN":
        raise HTTPException(
            detail="You don't have permission to access this service",
            status_code=status.HTTP_403_FORBIDDEN,
        )

    return await forward_request(request, f"{config.USER_SERVICE_URL}/users")


@router.api_route("/orders", methods=["GET", "POST"])
async def cr_orders(
    request: Request,
    current_user: Annotated[Dict[str, Any], Depends(get_current_user)],
):
    if current_user["role"] != "ADMIN":
        raise HTTPException(
            detail="You don't have permission to access this service",
            status_code=status.HTTP_403_FORBIDDEN,
        )

    return await forward_request(request, f"{config.ORDER_SERVICE_URL}/orders")


@router.api_route("/orders/{order_id}", methods=["GET", "PUT", "DELETE"])
async def rud_order(
    request: Request,
    order_id: int,
    current_user: Annotated[Dict[str, Any], Depends(get_current_user)],
):
    if current_user["role"] != "ADMIN":
        raise HTTPException(
            detail="You don't have permission to access this service",
            status_code=status.HTTP_403_FORBIDDEN,
        )

    return await forward_request(
        request,
        f"{config.ORDER_SERVICE_URL}/orders/{order_id}",
    )

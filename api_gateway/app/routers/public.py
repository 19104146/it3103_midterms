from fastapi import APIRouter, Request

from app.config import config
from app.proxy import forward_request

router = APIRouter()


@router.get("/products")
async def list_products(request: Request):
    return await forward_request(request, f"{config.PRODUCT_SERVICE_URL}/products")


@router.get("/products/{product_id}")
async def get_product(request: Request, product_id: int):
    return await forward_request(
        request,
        f"{config.PRODUCT_SERVICE_URL}/products/{product_id}",
    )


@router.post("/register")
async def register(request: Request):
    return await forward_request(request, f"{config.USER_SERVICE_URL}/register")


@router.post("/login")
async def login(request: Request):
    return await forward_request(request, f"{config.USER_SERVICE_URL}/login")

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from typing_extensions import List

from app.dependencies import get_product_service
from app.exceptions import ProductConflictException, ProductNotFoundException
from app.schemas import ProductRead, ProductWrite
from app.services import ProductService

router = APIRouter()


@router.get("/", response_model=List[ProductRead])
def list_products(
    product_service: ProductService = Depends(get_product_service),
) -> List[ProductRead]:
    return product_service.list_products()


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductWrite,
    product_service: ProductService = Depends(get_product_service),
) -> ProductRead:
    try:
        return product_service.create_product(product)
    except ProductConflictException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_409_CONFLICT)


@router.get("/{product_id}", response_model=ProductRead, status_code=status.HTTP_200_OK)
def read_product(
    product_id: int,
    product_service: ProductService = Depends(get_product_service),
) -> ProductRead:
    try:
        return product_service.read_product(product_id)
    except ProductNotFoundException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{product_id}", response_model=ProductRead, status_code=status.HTTP_200_OK)
def update_product(
    product_id: int,
    updated_product: ProductWrite,
    product_service: ProductService = Depends(get_product_service),
) -> ProductRead:
    try:
        return product_service.update_product(product_id, updated_product)
    except ProductNotFoundException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_404_NOT_FOUND)
    except ProductConflictException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_409_CONFLICT)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    product_service: ProductService = Depends(get_product_service),
) -> None:
    try:
        product_service.delete_product(product_id)
    except ProductNotFoundException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_404_NOT_FOUND)

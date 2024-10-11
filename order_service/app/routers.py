from fastapi import APIRouter, Depends, HTTPException, status
from requests.exceptions import HTTPError, RequestException
from typing_extensions import List

from app.dependencies import get_order_service
from app.exceptions import OrderNotFoundException
from app.schemas import OrderRead, OrderWrite
from app.services import OrderService

router = APIRouter()


@router.get("/", response_model=List[OrderRead])
def list_orders(order_service: OrderService = Depends(get_order_service)):
    return order_service.list_orders()


@router.post("/", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
def create_order(
    order: OrderWrite,
    order_service: OrderService = Depends(get_order_service),
) -> OrderRead:
    try:
        return order_service.create_order(order)
    except RequestException as e:
        if isinstance(e, HTTPError):
            raise HTTPException(status_code=e.response.status_code)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)


@router.get("/{order_id}", response_model=OrderRead)
def read_order(
    order_id: int,
    order_service: OrderService = Depends(get_order_service),
) -> OrderRead:
    try:
        return order_service.read_order(order_id)
    except OrderNotFoundException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{order_id}", response_model=OrderRead)
def update_order(
    order_id: int,
    order: OrderWrite,
    order_service: OrderService = Depends(get_order_service),
) -> OrderRead:
    try:
        return order_service.update_order(order_id, order)
    except OrderNotFoundException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_404_NOT_FOUND)
    except RequestException as e:
        if isinstance(e, HTTPError):
            raise HTTPException(status_code=e.response.status_code)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(
    order_id: int,
    order_service: OrderService = Depends(get_order_service),
) -> None:
    try:
        order_service.delete_order(order_id)
    except OrderNotFoundException as e:
        raise HTTPException(detail=e.message, status_code=status.HTTP_404_NOT_FOUND)

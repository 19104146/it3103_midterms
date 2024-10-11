import requests
from typing_extensions import List

from app.exceptions import OrderNotFoundException
from app.schemas import OrderItem, OrderRead, OrderWrite
from app.settings import settings


class OrderService:
    def __init__(self):
        self.orders: List[OrderRead] = []
        self.next_id: int = 1

    def list_orders(self) -> List[OrderRead]:
        return self.orders

    def create_order(self, order: OrderWrite) -> OrderRead:
        self._validate_user(order.user_key)
        self._validate_products(order.items)

        new_order = OrderRead(
            id=self.next_id,
            user_key=order.user_key,
            items=order.items,
        )

        self.orders.append(new_order)
        self.next_id += 1
        return new_order

    def read_order(self, order_id: int) -> OrderRead:
        existing_order = next((o for o in self.orders if o.id == order_id), None)
        if not existing_order:
            raise OrderNotFoundException()
        return existing_order

    def update_order(self, order_id: int, updated_order: OrderWrite) -> OrderRead:
        existing_order = self.read_order(order_id)

        self._validate_user(updated_order.user_key)
        self._validate_products(updated_order.items)

        existing_order.user_key = updated_order.user_key
        existing_order.items = updated_order.items
        return existing_order

    def delete_order(self, order_id: int) -> None:
        existing_order = self.read_order(order_id)
        self.orders.remove(existing_order)

    def _validate_user(self, user_key: int) -> None:
        response = requests.get(f"{settings.USER_SERVICE_URL}/users/{user_key}")
        response.raise_for_status()

    def _validate_products(self, items: List[OrderItem]) -> None:
        for item in items:
            response = requests.get(
                f"{settings.PRODUCT_SERVICE_URL}/products/{item.product_key}"
            )
            response.raise_for_status()

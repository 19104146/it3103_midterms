from typing_extensions import List

from app.exceptions import ProductConflictException, ProductNotFoundException
from app.schemas import ProductRead, ProductWrite


class ProductService:
    def __init__(self):
        self.products: List[ProductRead] = []
        self.next_id = 1

    def list_products(self) -> List[ProductRead]:
        return self.products

    def create_product(self, product: ProductWrite) -> ProductRead:
        if self._is_duplicate_name(product.name):
            raise ProductConflictException()

        new_product = ProductRead(
            id=self.next_id,
            name=product.name,
            price=product.price,
        )

        self.products.append(new_product)
        self.next_id += 1
        return new_product

    def read_product(self, product_id: int) -> ProductRead:
        existing_product = next((p for p in self.products if p.id == product_id), None)
        if not existing_product:
            raise ProductNotFoundException()
        return existing_product

    def update_product(
        self,
        product_id: int,
        updated_product: ProductWrite,
    ) -> ProductRead:
        existing_product = self.read_product(product_id)

        if existing_product.name != updated_product.name:
            if self._is_duplicate_name(updated_product.name):
                raise ProductConflictException()

        existing_product.name = updated_product.name
        existing_product.price = updated_product.price
        return existing_product

    def delete_product(self, product_id: int) -> None:
        existing_product = self.read_product(product_id)
        self.products.remove(existing_product)

    def _is_duplicate_name(self, name: str) -> bool:
        return any(p.name == name for p in self.products)

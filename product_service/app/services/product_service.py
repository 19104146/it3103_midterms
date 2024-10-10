from typing import List

from app.schemas.product import ProductRead, ProductWrite


class ProductService:
    def __init__(self):
        self.products: List[ProductRead] = []
        self.next_id = 1

    def _validate_unique_name(self, name: str) -> None:
        if any(p.name == name for p in self.products):
            raise ValueError("Product already exists")

    def create_product(self, product: ProductWrite) -> ProductRead:
        self._validate_unique_name(product.name)

        new_product = ProductRead(
            id=self.next_id,
            name=product.name,
            price=product.price,
        )

        self.products.append(new_product)
        self.next_id += 1
        return new_product

    def read_product(self, product_id: int) -> ProductRead:
        product = next((p for p in self.products if p.id == product_id), None)
        if not product:
            raise ValueError("Product not found")
        return product

    def update_product(
        self,
        product_id: int,
        updated_product: ProductWrite,
    ) -> ProductRead:
        existing_product = self.read_product(product_id)
        existing_product.name = updated_product.name
        existing_product.price = updated_product.price
        return existing_product

    def delete_product(self, product_id: int) -> None:
        product = self.read_product(product_id)
        self.products.remove(product)

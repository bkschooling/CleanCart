from models.product import Product
from typing import List

class Store:
    """
    Represents a store location with a list of products (inventory).
    """
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.inventory: List[Product] = []

    def add_product(self, product: Product):
        self.inventory.append(product)

    def get_product_info(self, product_name: str) -> List[Product]:
        return [
            p for p in self.inventory 
            if p.name.lower() == product_name.lower()
        ]

    def __repr__(self):
        return f"{self.name} in {self.location}"

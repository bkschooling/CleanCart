from models.store import Store
from models.product import Product
from typing import List, Tuple

class User:
    def __init__(self, name: str, home_city: str):
        self.name = name
        self.home_city = home_city
        self.cart: List[Tuple[Store, Product, int]] = []
        self.search_history: List[str] = []

    def add_to_cart(self, store: Store, product: Product, quantity: int = 1):
        self.cart.append((store, product, quantity))

    def calculate_total(self) -> float:
        return sum(product.price * qty for _, product, qty in self.cart)

    def log_search(self, product_name: str):
        self.search_history.append(product_name)

    def __repr__(self):
        return f"{self.name} from {self.home_city}"

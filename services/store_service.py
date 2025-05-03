from models.store import Store
from models.product import Product
import random
from typing import List, Tuple, Optional

def create_stores_and_inventory(store_data, product_prices) -> List[Store]:
    stores = [Store(name, location) for name, location in store_data]
    product_data = []

    for name, prices in product_prices.items():
        for price in prices:
            available = random.choices([True, False], weights=[0.8, 0.2])[0]
            product_data.append((name, price, available))

    for i, (name, price, available) in enumerate(product_data):
        store = stores[i % len(stores)]
        store.add_product(Product(name, price, available))

    return stores

def find_best_product(
    stores: List[Store], 
    product_name: str, 
    home_city: Optional[str] = None
) -> Optional[Tuple[Store, Product]]:
    best_option = None
    for store in stores:
        if home_city and store.location != home_city:
            continue
        for product in store.get_product_info(product_name):
            if product.availability:
                if not best_option or product.price < best_option[1].price:
                    best_option = (store, product)

    if not best_option and home_city:
        return find_best_product(stores, product_name, home_city=None)

    return best_option

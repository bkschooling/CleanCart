import csv
import json
from models.user import User
from utils.colors import colored

def export_user_data(user: User):
    if not user.cart:
        print(colored("⚠️ No items to export — your cart is empty.", "yellow"))
        return

    export_to_csv(user)
    export_to_json(user)

def export_to_csv(user: User, filename: str = "cart_export.csv"):
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Product", "Quantity", "Store", "City", "Price", "Subtotal"])
            for store, product, qty in user.cart:
                writer.writerow([
                    product.name, qty, store.name, store.location, 
                    f"${product.price:.2f}", f"${product.price * qty:.2f}"
                ])
        print(colored(f"✅ Cart exported to CSV: {filename}", "green"))
    except Exception as e:
        print(colored(f"❌ Failed to export CSV: {e}", "red"))

def export_to_json(user: User, filename: str = "cart_export.json"):
    try:
        data = []
        for store, product, qty in user.cart:
            item = {
                "product": product.name,
                "quantity": qty,
                "store": store.name,
                "city": store.location,
                "price": round(product.price, 2),
                "subtotal": round(product.price * qty, 2)
            }
            data.append(item)

        with open(filename, mode="w") as file:
            json.dump(data, file, indent=4)

        print(colored(f"✅ Cart exported to JSON: {filename}", "green"))
    except Exception as e:
        print(colored(f"❌ Failed to export JSON: {e}", "red"))

from models.user import User
from utils.colors import colored

def handle_cart_actions(user: User):
    if not user.cart:
        print(colored("🛒 Your cart is currently empty.", "yellow"))
        return

    print(colored("\n🧾 Your Shopping Cart:", "cyan"))
    for idx, (store, product, qty) in enumerate(user.cart, start=1):
        print(f"{idx}. {product.name} x{qty} @ ${product.price:.2f} "
              f"from {store.name} in {store.location} - "
              f"Subtotal: ${product.price * qty:.2f}")

    total = user.calculate_total()
    print(colored(f"\n💰 Total: ${total:.2f}", "green"))

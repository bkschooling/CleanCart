from models.user import User
from data.store_data import store_data
from data.product_prices import product_prices
from services.store_service import create_stores_and_inventory, find_best_product
from services.cart_service import handle_cart_actions
from services.export_service import export_user_data
from services.suggestion_service import suggest_products
from utils.logger import log_event
from utils.colors import colored

def run():
    print(colored("🛒 Welcome to Clean Cart 🛒", "cyan"))
    name = input("Enter your name: ").strip()
    city = input("Enter your home city: ").strip()
    user = User(name, city)

    stores = create_stores_and_inventory(store_data, product_prices)

    while True:
        print("\nWhat would you like to do?")
        print("1. Search for a product")
        print("2. View cart")
        print("3. Export cart")
        print("4. Get product suggestions")
        print("5. Exit")
        choice = input("Choose an option [1-5]: ").strip()

        if choice == "1":
            query = input("Enter product name: ").strip()
            user.log_search(query)
            log_event(f"{user.name} searched for '{query}'")

            best = find_best_product(stores, query, user.home_city)
            if best:
                store, product = best
                print(colored(f"✅ Found at {store.name} in {store.location}: {product}", "green"))
                add = input("Add to cart? (y/n): ").strip().lower()
                if add == 'y':
                    try:
                        qty = int(input("Enter quantity: ").strip())
                        user.add_to_cart(store, product, qty)
                    except ValueError:
                        print(colored("⚠️ Invalid quantity. Skipping.", "yellow"))
            else:
                print(colored("❌ Not available locally or globally.", "red"))

        elif choice == "2":
            handle_cart_actions(user)

        elif choice == "3":
            export_user_data(user)

        elif choice == "4":
            suggest_products(user)

        elif choice == "5":
            print(colored("👋 Thank you for using Clean Cart!", "cyan"))
            break

        else:
            print(colored("⚠️ Invalid choice. Please enter a number from 1 to 5.", "red"))

if __name__ == "__main__":
    run()

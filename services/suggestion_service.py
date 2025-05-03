from models.user import User
from collections import Counter
from utils.colors import colored

def suggest_products(user: User):
    if not user.search_history:
        print(colored("💡 No suggestions yet — search for some products first!", "yellow"))
        return

    print(colored("\n🧠 Based on your search history, you may also like:", "cyan"))

    suggestions = generate_suggestions(user.search_history)
    for idx, suggestion in enumerate(suggestions, start=1):
        print(f"{idx}. {suggestion}")

def generate_suggestions(search_history):

    related_products = {
        "pasta": ["sauce", "cheese", "bread"],
        "bread": ["butter", "jam", "cheese"],
        "milk": ["cereal", "cookies", "coffee"],
        "eggs": ["bacon", "cheese", "toast"],
        "chicken": ["rice", "spices", "lettuce"]
    }

    keywords = [p.lower() for p in search_history]
    suggestion_counter = Counter()

    for keyword in keywords:
        if keyword in related_products:
            suggestion_counter.update(related_products[keyword])

    return [item for item, _ in suggestion_counter.most_common(3)]

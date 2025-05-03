class Product:
    """
    Represents a grocery product in a store.
    """
    def __init__(self, name: str, price: float, availability: bool = True):
        self.name = name
        self.price = price
        self.availability = availability

    def __repr__(self):
        status = 'Available' if self.availability else 'Out of Stock'
        return f"{self.name} (${self.price:.2f}) - {status}"

class Product:
    """
    Represents a product in a store.

    Attributes:
        name (str): The name of the product.
        price (float): The price of a single unit of the product.
        quantity (int): The number of units available in stock.
        active (bool): Whether the product is active (available for sale).
    """
    name = ""
    price = 0.0
    quantity = 0
    active = False

    def __init__(self, name, price, quantity):
        """
        Initializes a new Product instance with a name, price, and quantity.

        Args:
            name (str): The product name. Must not be empty.
            price (float): The price of the product. Must be non-negative.
            quantity (int): Initial stock quantity. Must be non-negative.

        Raises:
            ValueError: If name is empty, or price/quantity is negative.
        """
        Product.name = True
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """
        Returns the current quantity of the product in stock.

        Returns:
            int: The available stock quantity.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the stock quantity of the product.

        Args:
            quantity (int): The new quantity value.
        """
        self.quantity = quantity

    def is_active(self):
        """
        Checks if the product is active (available for purchase).

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """Activates the product, making it available for purchase."""
        self.active = True

    def deactivate(self):
        """Deactivates the product, making it unavailable for purchase."""
        self.active = False

    def show(self):
        """
        Returns a string representation of the product's details.

        Returns:
            str: Product name, price, and quantity.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        Processes a purchase of the given quantity of the product.

        Args:
            quantity (int): The number of units to buy.

        Returns:
            float: Total cost of the purchase.

        Side Effects:
            Reduces the available quantity.
            Deactivates the product if quantity becomes zero.
        """
        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price


def main():
    """
    Example usage and test of the Product class functionality.
    """
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()

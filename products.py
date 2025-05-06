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
            print("1")
            raise ValueError("Name cannot be empty.")
        if price < 0:
            print("2")
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            print("3")
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

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

    def set_promotion(self, promotion):
        """
        Sets a promotion for the product.

        Args:
            promotion (Promotion): The promotion to apply.
        """
        self.promotion = promotion

    def get_promotion(self):
        """
        Gets the current promotion.

        Returns:
            Promotion or None: The current promotion if any.
        """
        return self.promotion


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
            str: Product name, price, quantity, and promotion.
        """
        promo_text = f" [Promotion: {self.promotion.name}]" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_text}"


    def buy(self, quantity):
        """
        Processes a purchase of the given quantity of the product.

        Args:
            quantity (int): The number of units to buy.

        Returns:
            float: Total cost of the purchase.

        Raises:
            ValueError: If the requested quantity exceeds available stock.
        """
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    """
    Represents a non-stocked product that has no inventory tracking,
    such as digital licenses.

    Attributes:
        Inherits all attributes from Product, but quantity is always 0.
    """

    def __init__(self, name, price):
        """
        Initializes a NonStockedProduct with no physical stock.

        Args:
            name (str): The product name.
            price (float): The price of the product.
        """
        super().__init__(name, price, quantity=0)

    def buy(self, quantity):
        """
        Processes a purchase without affecting quantity.

        Args:
            quantity (int): The number of units to buy.

        Returns:
            float: Total cost of the purchase.
        """
        return self.price * quantity

    def show(self):
        """
        Returns a string representation with a non-stocked note.

        Returns:
            str: Product details.
        """
        return f"{super().show()} (Non-stocked product)"


class LimitedProduct(Product):
    """
    Represents a product that has a per-order purchase limit,
    such as shipping fees.

    Attributes:
        maximum (int): The maximum quantity allowed per order.
    """

    def __init__(self, name, price, quantity, maximum):
        """
        Initializes a LimitedProduct with a purchase limit.

        Args:
            name (str): The product name.
            price (float): The price of the product.
            quantity (int): The stock quantity.
            maximum (int): The maximum quantity allowed per order.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """
        Processes a purchase with maximum quantity enforcement.

        Args:
            quantity (int): The number of units to buy.

        Returns:
            float: Total cost of the purchase.

        Raises:
            ValueError: If requested quantity exceeds maximum allowed.
        """
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot purchase more than {self.maximum} units of this product."
            )
        return super().buy(quantity)

    def show(self):
        """
        Returns a string representation with the max purchase note.

        Returns:
            str: Product details including max allowed quantity.
        """
        return f"{super().show()} (Maximum purchase quantity: {self.maximum})"


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

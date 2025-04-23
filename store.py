import products

class Store:
    """
    Represents a store that holds and manages a collection of products.

    Attributes:
        products (list): A list of Product objects available in the store.
    """
    def __init__(self, products):
        """
        Initializes a new Store instance.

        Args:
            products (list): A list of Product instances to populate the store.
        """
        self.products = products


    def add_product(self, product):
        """
        Adds a product to the store's inventory.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)


    def remove_product(self, product):
        """
        Removes a product from the store's inventory if it exists.

        Args:
            product (Product): The product to remove.
        """
        if product in self.products:
            self.products.remove(product)


    def get_total_quantity(self):
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: The sum of quantities for all products.
        """
        return sum(product.quantity for product in self.products)


    def get_all_products(self):
        """
        Retrieves all currently active products.

        Returns:
            list: A list of active Product objects.
        """
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list):
        """
        Processes a shopping list and calculates the total cost.

        Args:
            shopping_list (list): A list of tuples (Product, quantity).

        Returns:
            float: The total cost of all products in the shopping list.

        Side Effects:
            Reduces the stock of each product.
            May deactivate a product if its quantity becomes zero.
        """
        total = 0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total


def main():
    """
    Example usage and testing of the Store class.
    Initializes a store, shows total inventory, and processes an order.
    """
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products_list = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([
        (products_list[0], 1),
        (products_list[1], 2)
    ]))

if __name__ == "__main__":
    main()

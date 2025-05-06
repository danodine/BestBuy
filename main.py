import products
import store

# List of products available in the store
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

# Creating a store instance with the product list
best_buy = store.Store(product_list)


def start(store_obj):
    """
    Start the command-line interface for interacting with the store.

    Provides a menu-based system where the user can:
    1. List all products in the store.
    2. View the total quantity of items available in the store.
    3. Place an order by selecting products and quantities.
    4. Exit the program.

    Parameters:
        store_obj (store.Store): An instance of the Store class containing product data.
    """
    while True:
        print("\n==== Welcome to Best Buy ====")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\n--- Products in Store ---")
            for i, product in enumerate(store_obj.get_all_products(), start=1):
                print(f"{i}. {product.show()}")

        elif choice == "2":
            total = store_obj.get_total_quantity()
            print(f"\nTotal quantity in store: {total}")

        elif choice == "3":
            shopping_list = []
            active_products = store_obj.get_all_products()
            print("\n--- Make an Order ---")
            for i, product in enumerate(active_products, start=1):
                print(f"{i}. {product.show()}")

            while True:
                selection = input("Enter product number to buy (or 'done' to finish): ")
                if selection.lower() == 'done':
                    break
                try:
                    index = int(selection) - 1
                    if 0 <= index < len(active_products):
                        try:
                            quantity = int(input(f"Enter quantity for {active_products[index].name}: "))
                            product = active_products[index]

                            if isinstance(product, products.LimitedProduct) and quantity > product.maximum:
                                print(f"You can only purchase up to {product.maximum} units of {product.name}.")
                            elif quantity > product.get_quantity():
                                print(f"Not enough stock for {product.name}. Available: {product.get_quantity()}")
                            else:
                                shopping_list.append((product, quantity))
                        except ValueError:
                            print("Please enter a valid number.")
                    else:
                        print("Invalid product number.")
                except ValueError as err:
                    print(err)

            valid_shopping_list = []
            for product, quantity in shopping_list:
                if isinstance(product, products.LimitedProduct) and quantity > product.maximum:
                    print(f"Cannot order more than {product.maximum} units of {product.name}. Skipping.")
                elif product.get_quantity() < quantity:
                    print(f"Not enough stock for {product.name}. Available: {product.get_quantity()}. Skipping.")
                else:
                    valid_shopping_list.append((product, quantity))

            if valid_shopping_list:
                try:
                    total_cost = store_obj.order(valid_shopping_list)
                    print(f"\nOrder placed! Total cost: ${total_cost:.2f}")
                except Exception as e:
                    print(f"Order failed: {e}")
            else:
                print("No valid items to order.")

        elif choice == "4":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Starts the store interface when script is run directly
    start(best_buy)

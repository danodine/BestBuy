import products
import store

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)


def start(store_obj):
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
                        quantity = int(input(f"Enter quantity for {active_products[index].name}: "))
                        shopping_list.append((active_products[index], quantity))
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Please enter valid numbers.")

            try:
                total_cost = store_obj.order(shopping_list)
                print(f"\nOrder placed! Total cost: ${total_cost:.2f}")
            except Exception as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    start(best_buy)

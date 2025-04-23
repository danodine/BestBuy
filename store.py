import products

class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        return sum(product.quantity for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        total = 0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total

def main():
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

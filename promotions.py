from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for all promotions.
    """

    def __init__(self, name):
        """
        Initializes the promotion with a name.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Calculates the price after applying the promotion.

        Args:
            product (Product): The product the promotion is applied to.
            quantity (int): The number of units being purchased.

        Returns:
            float: The total price after discount.
        """
        pass


class PercentDiscount(Promotion):
    """
    A promotion that gives a percentage discount on the total.
    """

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * quantity * (1 - self.percent / 100)
        return discounted_price


class SecondHalfPrice(Promotion):
    """
    A promotion where every second item is half price.
    """

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        total = (full_price_items * product.price) + (half_price_items * product.price * 0.5)
        return total


class ThirdOneFree(Promotion):
    """
    A promotion where for every 3 items, the third one is free.
    """

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        total_price = (quantity - free_items) * product.price
        return total_price

# test_product.py

import pytest
from products import Product

def test_create_valid_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.active is True

def test_create_product_with_empty_name_raises_exception():
    with pytest.raises(ValueError, match="Name cannot be empty."):
        Product("", price=1450, quantity=100)

def test_create_product_with_negative_price_raises_exception():
    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)

def test_create_product_with_negative_quantity_raises_exception():
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("MacBook Air M2", price=1000, quantity=-5)

def test_product_becomes_inactive_when_quantity_is_zero():
    product = Product("MacBook Air M2", price=1000, quantity=1)
    product.buy(1)
    assert product.quantity == 0
    assert not product.is_active()

def test_product_purchase_reduces_quantity_and_returns_total_price():
    product = Product("MacBook Air M2", price=1000, quantity=10)
    total = product.buy(3)
    assert total == 3000
    assert product.quantity == 7

def test_buying_more_than_available_quantity_raises_exception():
    product = Product("MacBook Air M2", price=1000, quantity=5)
    # Product class currently does NOT raise an exception in this case.
    # This will fail unless you add this check in buy()
    with pytest.raises(ValueError, match="Not enough stock available."):
        product.buy(6)

"""
This script asks the user which items he wants to buy and calculates the
total value of the purchase.
"""
from decimal import Decimal


class Product:
    """Product class."""
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Cart:
    """Cart class."""
    def __init__(self, name, items=None):
        self.name = name
        self.items = items if items is not None else []
    

    def calculate_total(self):
        """Calculate the total value of the cart."""
        total = 0
        for product_code, quantity in self.items:
            product = products[product_code]
            total += product.value * quantity
        return total

products = {
    "1": Product("Maça", Decimal(4.5)),
    "2": Product("Melancia", Decimal(6.3))
}

print("Hello client, welcome to our store!")
print("Here are the products we have available:")

for code, product in products.items():
    print(f"{code} -> {product.name} - R$ {product.value:.2f}")

name = input("What's your name? ").strip()
cart = Cart(name)

while True:
    product_code = input("Product code (or press enter to finish): ").strip()
    if not product_code:
        break
    if product_code not in products:
        print("Invalid product code.")
        continue
    quantity = int(input("Quantity: ").strip())
    cart.items.append([product_code, quantity])

print(f"Hello {cart.name}!")
print(f"In your cart you have {len(cart.items)} item(s).")
print(f"Total value: R$ {cart.calculate_total():.2f}")



# cart.py
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not item.is_out_of_stock:  # Check if the item is not out of stock
            self.items.append(item)
        else:
            print(f"Cannot add {item.name} to the cart because it is out of stock.")

    def is_empty(self):
        return len(self.items) == 0

    def calculate_total(self):
        return sum(item.price for item in self.items)

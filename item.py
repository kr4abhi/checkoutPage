# item.py
class Item:
    def __init__(self, name, price, is_out_of_stock=False):
        self.name = name
        self.price = price
        self.is_out_of_stock = is_out_of_stock
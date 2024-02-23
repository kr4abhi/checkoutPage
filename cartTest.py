import unittest
from cart import Cart
from item import Item

class TestCart(unittest.TestCase):

    def test_single_item_added(self):
        item = Item("Item 1", 10)

        cart = Cart()

        cart.add_item(item)

        self.assertEqual(len(cart.items), 1, "Single item should be added to the cart")

    def test_multiple_items_added(self):
        # Create multiple items
        items = [
            Item("Item 1", 10),
            Item("Item 2", 20)
        ]

        # Create a cart
        cart = Cart()

        # Add multiple items to the cart
        for item in items:
            cart.add_item(item)

        # Verify that all items were added to the cart
        self.assertEqual(len(cart.items), len(items), "Multiple items should be added to the cart")

    def test_out_of_stock_item(self):
        # Create an out-of-stock item
        out_of_stock_item = Item("Out of Stock Item", 10, is_out_of_stock=True)

        # Create a cart
        cart = Cart()

        # Attempt to add the out-of-stock item to the cart
        cart.add_item(out_of_stock_item)

        # Verify that the item was not added to the cart
        self.assertEqual(len(cart.items), 0, "Out-of-stock item should not be added to the cart")

    def test_mixed_items(self):
        # Create items
        in_stock_item = Item("In Stock Item", 20)
        out_of_stock_item = Item("Out of Stock Item", 10, is_out_of_stock=True)

        # Create a cart
        cart = Cart()

        # Add items to the cart
        cart.add_item(in_stock_item)
        cart.add_item(out_of_stock_item)

        # Verify that only the in-stock item was added to the cart
        self.assertEqual(len(cart.items), 1, "Only in-stock item should be added to the cart")

if __name__ == '__main__':
    unittest.main()

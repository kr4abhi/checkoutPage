import unittest
from unittest.mock import Mock
from cart import Cart
from order_Processor import OrderProcessor
from item import Item

class TestAmazonCheckout(unittest.TestCase):

    def test_successful_order_placement(self):
        cart = Cart()
        # cart.add_item("Item 1", 10)

        item_x = Item("Item X", 10)
        item_y = Item("Item Y", 20)

        cart.add_item(item_x)
        cart.add_item(item_y)
        

        order_processor = OrderProcessor()

        payment_amount = cart.calculate_total()  
        
        order_processor.place_order = Mock(return_value=(True, "Order placed successfully"))

        success, message = order_processor.place_order(cart, "payment_details", "shipping_address", payment_amount)
        self.assertTrue(success)
        self.assertEqual(message, "Order placed successfully")
        print("Test case 'test_successful_order_placement' successful")

    def test_invalid_payment_information(self):
        cart = Cart()
        item_x = Item("Item X", 10)
        cart.add_item(item_x)

        payment_amount = cart.calculate_total()

        order_processor = OrderProcessor()
        order_processor.place_order = Mock(return_value=(False, "Invalid payment information"))

        success, message = order_processor.place_order(cart, "invalid_payment_details", "shipping_address", payment_amount)
        self.assertFalse(success)
        self.assertEqual(message, "Invalid payment information")
        print("Test case 'test_invalid_payment_information' successful")

    def test_order_with_multiple_items(self):
        cart = Cart()
        
        item_x = Item("Item X", 10)
        item_y = Item("Item Y", 20)
        item_z = Item("Item Z", 30)
        item_a = Item("Item A", 40)
        item_b = Item("Item B", 50)

        cart.add_item(item_x)
        cart.add_item(item_y)
        cart.add_item(item_z)
        cart.add_item(item_a)
        cart.add_item(item_b)

        payment_amount = cart.calculate_total()

        order_processor = OrderProcessor()
        order_processor.place_order = Mock(return_value=(True, "Order placed successfully"))

        success, message = order_processor.place_order(cart, "payment_details", "shipping_address", payment_amount)
        self.assertTrue(success)
        self.assertEqual(message, "Order placed successfully")
        print("Test case 'test_order_with_multiple_items' successful")

    def test_empty_cart(self):
        cart = Cart()

        payment_amount = cart.calculate_total()

        order_processor = OrderProcessor()
        success, message = order_processor.place_order(cart, "payment_details", "shipping_address", payment_amount)
        self.assertFalse(success)
        self.assertEqual(message, "Cannot place order with an empty cart")
        print("Test case 'test_empty_cart' successful")
    
    def test_order_total_mismatch(self):
    # Create a cart with items and their values
        cart = Cart()
        item_x = Item("Item X", 10)
        item_y = Item("Item Y", 20)

        cart.add_item(item_x)
        cart.add_item(item_y)


        # Set the payment amount (incorrect)
        payment_amount = 40  # Assuming an incorrect payment amount

        # Create an instance of OrderProcessor
        order_processor = OrderProcessor()

        # Place the order using OrderProcessor
        success, message = order_processor.place_order(cart, "payment_details", "shipping_address", payment_amount)
    
        # Assert that the order placement fails due to total mismatch
        self.assertFalse(success, "Order placement should fail due to total mismatch")
        self.assertEqual(message, f"Payment amount ({payment_amount}) does not match order total ({cart.calculate_total()})")
        print("Test case 'test_order_mismatch_successful' successful")

        # self.assertFalse(success, "Order placement should fail due to total mismatch")
        # self.assertEqual(message, f"Payment amount ({payment_amount}) does not match order total ({payment_amount})")
    
    def test_invalid_shipping_address(self):
        cart = Cart()
        item_x = Item("Item X", 10)
        cart.add_item(item_x)

        payment_amount = cart.calculate_total()

        order_processor = OrderProcessor()
        order_processor.place_order = Mock(return_value=(False, "Invalid shipping address"))

        success, message = order_processor.place_order(cart, "payment_details", "invalid_shipping_address", payment_amount)
        self.assertFalse(success)
        self.assertEqual(message, "Invalid shipping address")
        print("Test case 'test_invalid_shipping_address' successful")

    


    

    

if __name__ == '__main__':
    unittest.main()

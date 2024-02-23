# order_processor.py
class OrderProcessor:
    def place_order(self, cart, payment_details, shipping_address, payment_amount):
        # Simulate placing the order
        if cart.is_empty():
            return False, "Cannot place order with an empty cart"
        
        item_total = cart.calculate_total()
        # item_total = sum(value for item, value in cart.items)
        
        if item_total != payment_amount:
            return False, f"Payment amount ({payment_amount}) does not match order total ({item_total})"

        # Simulate processing payment and shipping
        # For simplicity, let's assume payment and shipping are successful
        return True, "Order placed successfully"

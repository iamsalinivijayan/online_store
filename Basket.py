from Item import *
class Basket:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        #print(f"Item {item.product.get_name()} added to the basket.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            #print(f"Item {item.product.get_name()} removed from the basket.")
        else:
            print("Item not found in the basket.")

    def calculate_total(self):
        total = 0.0
        for item in self.items:
            total += item.product.get_price() * item.quantity
        return total
    
    def calculate_total_items(self):
        items = 0
        for item in self.items:
            items = items + item.quantity
        return items
    
    def calculate_gift_wrapping_charge(self):
        gift_charge = 0
        for item in self.items:
            if item.gift_wrap == 'Y':
                gift_charge=gift_charge+item.quantity
            else:
                pass
        return gift_charge  
    
    def calculate_shipping_fee(self):
        shipping_fee=0
        total_items=self.calculate_total_items()
        if total_items%10 == 0:
            shipping_fee=(total_items/10)*5
        else:
            shipping_fee=((total_items/10)+1)
        return shipping_fee

    def display_basket(self):
        if self.items:
            print("Basket:")
            for item in self.items:
                print(f"Product: {item.product.get_name()}, Price: {item.product.get_price()}, Quantity: {item.quantity} , Total price: {item.quantity*item.product.get_price()}")
        else:
            print("Basket is empty.")
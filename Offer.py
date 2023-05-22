from Basket import *
class Offer:
    def __init__(self, Basket):
        self.basket = Basket

    def flat_10_discount(self):
        discount = 0
        if self.basket.calculate_total() > 200:
            discount = 10
        else:
            pass
        return discount
            
        

    def bulk_5_discount(self):
        discount=0
        for item in self.basket.items:
            if item.quantity > 10:
                discount = discount + item.product.get_price()*.05 * item.quantity
            else:
                pass
        return discount


    def bulk_10_discount(self):
        discount=0
        if self.basket.calculate_total_items() > 20:
            discount = discount + self.basket.calculate_total()*.10
        else:
            pass
        return discount
          
    def tiered_50_discount(self):
        discount=0
        if self.basket.calculate_total_items() > 30:
            for item in self.basket.items:
                if item.quantity > 15:
                    discount = discount + item.product.get_price()*.50* (item.quantity-15)
        return discount

    def apply_offer(self):
        offer_list = {}
        offer_list["flat_10_discount"] = self.flat_10_discount()
        offer_list["bulk_5_discount"] = self.bulk_5_discount()
        offer_list["bulk_10_discount"] = self.bulk_10_discount()
        offer_list["tiered_50_discount"] = self.tiered_50_discount()
        sorted_offer={offer_name: discount for offer_name, discount in sorted(offer_list.items(), key=lambda item: item[1])}
        return sorted_offer  
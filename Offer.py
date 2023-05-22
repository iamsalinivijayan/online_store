from Basket import *
# class Offer
class Offer:
    def __init__(self, Basket):
        self.basket = Basket

    # flat_10_discount function is used if the cart total exceeds 200 discount of 10$ is given
    def flat_10_discount(self):
        discount = 0
        if self.basket.calculate_total() > 200:
            discount = 10
        else:
            pass
        return discount

    '''bulk_5_discount function is used when any one of the product quantity exceeds 10 a 5% discount is provided on 
    that items total price'''
    def bulk_5_discount(self):
        discount=0
        for item in self.basket.items:
            if item.quantity > 10:
                discount = discount + item.product.get_price()*.05 * item.quantity
            else:
                pass
        return discount

    '''bulk_10_discount is applied when the total quantity of products in the cart exceeds 20, 10% discount on the cart
    total is given'''
    def bulk_10_discount(self):
        discount=0
        if self.basket.calculate_total_items() > 20:
            discount = discount + self.basket.calculate_total()*.10
        else:
            pass
        return discount
    '''tiered_50_discount function, if the total quantity of products exceeds 30 and any single product quantity greater
    greater than 15 then a 50% discount is provided on the items above 15 and the price remains same for the first 15 
    items'''
    def tiered_50_discount(self):
        discount=0
        if self.basket.calculate_total_items() > 30:
            for item in self.basket.items:
                if item.quantity > 15:
                    discount = discount + item.product.get_price()*.50* (item.quantity-15)
        return discount
    # applying and sorting the discounts
    def apply_offer(self):
        offer_list = {}
        offer_list["flat_10_discount"] = self.flat_10_discount()
        offer_list["bulk_5_discount"] = self.bulk_5_discount()
        offer_list["bulk_10_discount"] = self.bulk_10_discount()
        offer_list["tiered_50_discount"] = self.tiered_50_discount()
        sorted_offer={offer_name: discount for offer_name, discount in sorted(offer_list.items(), key=lambda item: item[1])}
        return sorted_offer  

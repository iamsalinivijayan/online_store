from Offer import *
# class App
class App:
    productA = Product("A", 20)
    productB = Product("B", 40)
    productC = Product("C", 50)

    # Taking number of quantity the users want to purchase and allocating it to the respective variables
    number_of_A = int(input("Enter the number of product A you want: "))
    gift_wrapping_required_A = input("Gift wrapping required? Y or N: ").upper()
    number_of_B = int(input("Enter the number of product B you want: "))
    gift_wrapping_required_B = input("Gift wrapping required? Y or N: ").upper()
    number_of_C = int(input("Enter the number of product C you want: "))
    gift_wrapping_required_C = input("Gift wrapping required? Y or N: ").upper()

    '''hard coded data for debugging purpose
    number_of_A=10
    gift_wrapping_required_A='N'
    number_of_B=40
    gift_wrapping_required_B='Y'
    number_of_C=10
    gift_wrapping_required_C='Y'
    '''
    
    # calling Basket function
    basket = Basket()

    # adding item to the basket
    basket.add_item(Item(productA,number_of_A,gift_wrapping_required_A))
    basket.add_item(Item(productB,number_of_B,gift_wrapping_required_B))
    basket.add_item(Item(productC,number_of_C,gift_wrapping_required_C))
    
    basket.display_basket()
    # assigning the values from the functions to find calculate total price, shipping fee and gift wrapping fee
    total_price = basket.calculate_total()
    shipping_fee = basket.calculate_shipping_fee()
    gift_wrapping_charges = basket.calculate_gift_wrapping_charge()

    # printing the invoice
    print("Subtotal: $",total_price)
    ofr = Offer(basket)
    discount_applied=ofr.apply_offer().popitem()
    total = total_price - discount_applied[1] + shipping_fee + gift_wrapping_charges
    print(f"Discount {discount_applied[0]} applied -${discount_applied[1]}" )
    print("Shipping fee : $",shipping_fee)
    print("Gift wrap fee : $",gift_wrapping_charges)
    print("Total : $",total)
    
    

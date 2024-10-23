class shop:
    def grocery_items(self):
        print('Grocery')
    def food_items(self):
        print('food_items')
class staff(shop):
    def customer_service(self):
        print('Customer Service')
    def additional_offers(self):
        print('additional Offers')
class customer(shop):
    def card(self):
        print('card')
    def cash(self):
        print('cash')
        
    
cust1=customer()
cust1.grocery_items()
cust1.card()

staff1=staff()
staff1.food_items()

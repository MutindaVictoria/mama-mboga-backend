class Groceries:
    def __init__(self, names, prices):
        self.names = names
        self.prices = prices

class Order:
    def __init__(self):
        self.products = []

    def add_item(self,item):
        self.product.append(item)
    
    def view_cart(self):
        for item in self.product:
            print(item)
    
    def place_order(self):
        self.total_price=0
        for item in self.product:
            total_price +=item.price
            print(f"Item Name:{item.name}Price:{item.price}")
            print(f"Total Price:{self.total_price}")
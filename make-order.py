class Groceries:
    def__init__(self,name,price):
        self.name=name
        self.price=price

class Order:
    def__init__(self):
        self.product=[]

    def add_item(self,item):
        self.product.append(item)
    
    def view_cart(self):
        for item in self.product:
            print(f"The items in the cart are:{self.product}")
    
    def place_order(self):
        self.total_price=0
        for item in self.product:
            total_price +=item.price
            print(f" {item.name}  price is:{item.price}")
            print(f"Total price of {item.name} is:{self.total_price}")
class Groceries:
    def__init__(self,name,price):
        self.name=name
        self.price=price

class Order:
    def__init__(self):
        self.product=[]

    def add_item(self,item):
        self.product.append(item)
        return f"The:{item}has been successfully been added to the cart"
    
    def view_cart(self):
        for item in self.product:
            print(f"The items available in the cart are:{self.product}")
    
    def place_order(self):
        self.total_price=0
        for item in self.product:
            total_price +=item.price
            print(f"You ordered: {item.name} ,the price is:{item.price}")
            print(f"The total price for the order is:{self.total_price}")
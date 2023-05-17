class Product:
    def__init__(self,name,price,image,quantity):
        self.name = name
        self.price=price
        self.image=image
        self.quantity=quantity

class Cart:
    def__init__(self):
        self.product=[]
        self.total=0
    def add_items(self,item):
        self.product.append(item)
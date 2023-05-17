class Product:
    def __init__(self, name, price, image, quantity):
        self.name = name
        self.price = price
        self.image = image
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.products = []
        self.total = 0

    def add_items(self, item):
        self.products.append(item)
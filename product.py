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
    def remove_items(self, item):  # Enables the client to remove items from the cart
        if item in self.product:
            self.product.remove(item)
        else:
            print("Item not found in cart.")
    def get_total_items(self):  # Enables the client to get the total number of items in the cart
        return len(self.product)
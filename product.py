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
            print("Item not found in cart,the items in the cart are:{item}")

    def get_total_items(self):  # Enables the client to get the total number of items in the cart
        return len(f "The itemss in the cart are:{self.product}

    def total_amount_of_item(self):  # Enables the client to get the total price of items in cart
        total_price = 0
        for item in self.product:
            total_price += item.price
        return f"The total price of items in the cart is:{total_price}"
        

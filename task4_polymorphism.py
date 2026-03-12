class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        print(self.name, self.price)


class Laptop(Product):

    def get_info(self):
        print("Laptop:", self.name, self.price)


class Mobile(Product):

    def get_info(self):
        print("Mobile:", self.name, self.price)


items = [
    Laptop("Dell", 70000),
    Mobile("Samsung", 25000)
]

for item in items:
    item.get_info()
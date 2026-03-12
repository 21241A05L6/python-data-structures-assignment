class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        self.products = [p for p in self.products if p.name != name]

    def get_total_value(self):
        total = 0
        for p in self.products:
            total += p.price
        return total

    def show_all_products(self):
        for p in self.products:
            print(p.name, p.price)


class Store:

    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Product name: ")
        price = float(input("Price: "))

        product = Product(name, price)

        self.inventory.add_product(product)

    def show_summary(self):
        print("Total items:", len(self.inventory.products))
        print("Total value:", self.inventory.get_total_value())


store = Store("Tech Store")

for i in range(3):
    store.add_new_product()

store.inventory.show_all_products()

store.show_summary()
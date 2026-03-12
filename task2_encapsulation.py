class Product:

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price


p = Product("Keyboard", 1500)

print("Price:", p.get_price())

p.set_price(2000)

print("Updated price:", p.get_price())
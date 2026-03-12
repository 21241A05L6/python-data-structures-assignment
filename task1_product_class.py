class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(self.name, self.price, self.category)

    def apply_discount(self, percent):
        return self.price - (self.price * percent / 100)


p1 = Product("Laptop", 60000, "Electronics")
p2 = Product("Mouse", 500, "Accessories")

p1.get_info()
p2.get_info()

print("Discounted price:", p1.apply_discount(10))
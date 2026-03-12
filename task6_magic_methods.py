class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    def __add__(self, other):
        return self.price + other.price


p1 = Product("Laptop", 60000, "Electronics")
p2 = Product("Mobile", 20000, "Electronics")

print(p1)

print("Total price:", p1 + p2)
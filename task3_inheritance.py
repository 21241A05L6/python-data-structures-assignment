class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        print(self.name, self.price)


class ElectronicProduct(Product):

    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    def get_info(self):
        print(self.name, self.price, "Warranty:", self.warranty_years)


item = ElectronicProduct("TV", 45000, 2)

item.get_info()
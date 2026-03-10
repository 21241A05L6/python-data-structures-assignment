# Task 1: Product Collections (Lists & Tuples)

products = ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse", "Monitor"]

sample_product = ("Laptop", 75000, "Electronics")

print("Second product:", products[1])
print("Last product:", products[-1])

products.append("Tablet")
products.append("Smartwatch")

print("Updated products:", products)

sample_list = list(sample_product)
sample_list[1] = 70000
sample_product = tuple(sample_list)

print("Updated sample product:", sample_product)
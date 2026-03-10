products = ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse", "Monitor"]

categories = ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Electronics"]

price_dict = {
    "Laptop": 75000,
    "Phone": 30000,
    "Headphones": 2000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}

catalog = []

for i in range(len(products)):
    name = products[i]
    price = price_dict[name]
    category = categories[i]
    catalog.append((name, price, category))

print("Catalog:", catalog)

category_to_products = {}

for name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(name)

print(category_to_products)

max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))

print("Category with most products:", max_category)
print("Products:", category_to_products[max_category])
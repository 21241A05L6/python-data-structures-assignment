products = ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse", "Monitor"]

categories = ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Electronics"]

categories_set = set(categories)

print("Unique categories:", categories_set)

categories_set.add("Gaming")
categories_set.add("Electronics")

print("Updated categories:", categories_set)

print("Is 'Gaming' present?", "Gaming" in categories_set)

print("Total unique categories:", len(categories_set))
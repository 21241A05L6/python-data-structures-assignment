price_dict = {
    "Laptop": 75000,
    "Phone": 30000,
    "Headphones": 2000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}

price_dict["Tablet"] = 25000

price_dict["Mouse"] = 900

product = "Keyboard"

if product in price_dict:
    del price_dict[product]

average_price = sum(price_dict.values()) / len(price_dict)

print("Average price:", average_price)

max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most expensive:", max_product)
print("Cheapest:", min_product)
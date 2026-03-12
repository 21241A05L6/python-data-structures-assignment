# Task 5: Safe Shopping Cart

cart = []

while True:

    value = input("Enter price (or q to quit): ")

    if value == "q":
        break

    try:

        price = float(value)

        if price < 0:
            raise ValueError("Price cannot be negative")

        cart.append(price)

    except ValueError as e:
        print("Invalid input:", e)


print("Total items:", len(cart))
print("Total bill:", sum(cart))
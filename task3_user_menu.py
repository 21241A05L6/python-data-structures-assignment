# Task 3: User Menu

orders = []

while True:

    print("\nMenu")
    print("1 - Add order amount")
    print("2 - Show all orders and totals")
    print("q - Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = input("Enter order amount: ")

        if not amount.isdigit():
            print("Invalid input")
            continue

        orders.append(int(amount))

    elif choice == "2":

        total = 0

        for order in orders:

            if order >= 2000:
                discount = 0.15
            elif order >= 1500:
                discount = 0.10
            elif order >= 1000:
                discount = 0.07
            else:
                discount = 0

            final = order - (order * discount)

            print(order, "->", final)

            total += final

        print("Total:", total)

    elif choice == "q":
        break

    else:
        print("Invalid option")
        continue
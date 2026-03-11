# Task 7: Menu Using Functions

prices = []

def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):

    if len(prices_list) == 0:
        return 0

    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):

    if len(prices_list) == 0:
        return 0

    return max(prices_list)


while True:

    print("\nMenu")
    print("1 - Add price")
    print("2 - Show average price")
    print("3 - Show highest price")
    print("q - Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        price = float(input("Enter price: "))
        add_price(prices, price)

    elif choice == "2":
        print("Average price:", get_average_price(prices))

    elif choice == "3":
        print("Highest price:", get_max_price(prices))

    elif choice == "q":
        break

    else:
        print("Invalid option")
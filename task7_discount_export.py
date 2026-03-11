# Task 7: Export Discounted Prices

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

with open("discount_report.txt", "w") as file:

    file.write("Product | Original Price | Discounted Price\n")

    total = 0
    count = 0

    for product, price in prices.items():

        discounted = price - (price * discount / 100)

        file.write(product + " | " + str(price) + " | " + str(discounted) + "\n")

        total += discounted
        count += 1

    average = total / count

    file.write("\nTotal Items: " + str(count))
    file.write("\nAverage Discounted Price: " + str(average))

with open("discount_report.txt", "r") as file:
    print(file.read())
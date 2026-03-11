# Task 5: Create Product Info File

with open("products.txt", "w") as file:

    for i in range(3):
        name = input("Enter product name: ")
        price = input("Enter price: ")

        file.write(name + " | " + price + "\n")

with open("products.txt", "r") as file:

    print("Product List:")
    for line in file:
        print(line.strip())
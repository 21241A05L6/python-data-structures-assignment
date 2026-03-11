# Task 2: Read File in Different Ways

with open("sales_data.txt", "r") as file:
    print("Using read():")
    print(file.read())

with open("sales_data.txt", "r") as file:
    print("Using readline():")
    print(file.readline())

with open("sales_data.txt", "r") as file:
    lines = file.readlines()

sales_list = [int(line.strip()) for line in lines]

print("Sales List:", sales_list)
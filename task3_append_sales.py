# Task 3: Append New Sales

new_sales = [5000, 2500, 1700]

with open("sales_data.txt", "a") as file:
    for sale in new_sales:
        file.write(str(sale) + "\n")

with open("sales_data.txt", "r") as file:
    lines = file.readlines()

print("Updated File:")
for line in lines:
    print(line.strip())

print("Total Lines:", len(lines))
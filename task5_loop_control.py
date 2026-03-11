# Task 5: Loop Control

daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for day in daily:

    if day == -1:
        print("Corrupted data found. Stopping.")
        break

    if day == 0:
        print("No sales today")
        continue

    total_sales += day

    print("Added:", day, "Running Total:", total_sales)

print("Final Total Sales:", total_sales)
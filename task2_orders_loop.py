# Task 2: Process Multiple Orders

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

for order_amount in orders:

    if order_amount >= 2000:
        discount = 0.15
    elif order_amount >= 1500:
        discount = 0.10
    elif order_amount >= 1000:
        discount = 0.07
    else:
        discount = 0

    discount_amount = order_amount * discount
    final_amount = order_amount - discount_amount

    if discount > 0:
        discounted_orders += 1

    total_revenue += final_amount

    print(order_amount, "->", discount_amount, "->", final_amount)

print("Total Revenue:", total_revenue)
print("Orders with discount:", discounted_orders)
# Task 1: Discount Rules

order_amount = input("Enter order amount: ")

# Check if numeric
if not order_amount.isdigit():
    print("Error: Please enter a valid number")
else:
    order_amount = int(order_amount)

    if order_amount >= 2000:
        discount = 0.15
    elif order_amount >= 1500:
        discount = 0.10
    elif order_amount >= 1000:
        discount = 0.07
    else:
        discount = 0

    discount_amount = order_amount * discount
    subtotal = order_amount - discount_amount

    tax = subtotal * 0.05
    final_total = subtotal + tax

    print("Order Amount:", order_amount)
    print("Discount:", discount_amount)
    print("Subtotal:", subtotal)
    print("Tax (5%):", tax)
    print("Final Total:", final_total)
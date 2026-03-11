# Task 1: Price After Discount

def apply_discount(price, discount_percent=5):

    if discount_percent > 60:
        print("Discount cannot exceed 60%")
        return price

    final_price = price - (price * discount_percent / 100)
    return final_price


print(apply_discount(1000, 10))
print(apply_discount(500))
# Task 2: Bill Calculator

prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for price in prices:

    try:
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be numeric")

        if price < 0:
            raise ValueError("Negative price not allowed")

        total += price

    except TypeError:
        print("Skipping invalid type:", price)

    except ValueError as e:
        print("Skipping:", e)

print("Total Bill:", total)
# Task 5: Filter Expensive Products

prices = [100, 250, 400, 1200, 50, 2000, 850]

greater_than_500 = list(filter(lambda x: x > 500, prices))

less_equal_500 = list(filter(lambda x: x <= 500, prices))

print("Prices > 500:", greater_than_500)
print("Prices <= 500:", less_equal_500)
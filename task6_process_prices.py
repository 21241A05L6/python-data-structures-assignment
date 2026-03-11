# Task 6: Process Prices

def process_prices(prices):

    discounted_prices = list(map(lambda x: x - x * 0.10, prices))

    filtered_prices = list(filter(lambda x: x > 300, discounted_prices))

    return discounted_prices, filtered_prices


result = process_prices([100, 500, 900, 50, 750])

print("Discounted Prices:", result[0])
print("Filtered Prices:", result[1])
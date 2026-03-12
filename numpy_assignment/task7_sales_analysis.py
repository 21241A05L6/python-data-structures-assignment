import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

print("Total weekly sales:", np.sum(sales))

print("Average daily sales:", np.mean(sales))

print("Highest sales:", np.max(sales))
print("Lowest sales:", np.min(sales))

print("Standard deviation:", np.std(sales))

average = np.mean(sales)

days_above_avg = sales[sales > average]

print("Days above average:", days_above_avg)
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Row-wise sum:", np.sum(data, axis=1))
print("Column-wise sum:", np.sum(data, axis=0))

print("Minimum:", np.min(data))
print("Maximum:", np.max(data))

print("Overall mean:", np.mean(data))
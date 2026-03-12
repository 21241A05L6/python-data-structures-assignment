import numpy as np

# 1D array from 1 to 10
arr1 = np.arange(1, 11)

# 2D array (3x3)
arr2 = np.arange(1, 10).reshape(3, 3)

# array from list
arr3 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)

print("\nArray 2:\n", arr2)
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)

print("\nArray 3:", arr3)
print("Shape:", arr3.shape)
print("Data Type:", arr3.dtype)
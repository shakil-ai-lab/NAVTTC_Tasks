import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# 1D indexing from a flattened view
print(arr[0, 1])  # 20
print(arr[2, 0])  # 70

# slice a row
print("row 1:", arr[1])

# access elements with negative indices
print("last element:", arr[-1, -1])

# boolean indexing
mask = arr > 50
print("mask:\n", mask)
print("values > 50:", arr[mask])

# fancy indexing
print("first and last row:\n", arr[[0, 2]])
print("first and third column:\n", arr[:, [0, 2]])

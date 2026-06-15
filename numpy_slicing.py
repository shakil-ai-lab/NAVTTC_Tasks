import numpy as np

arr = np.arange(1, 13).reshape(3, 4)
print("arr:\n", arr)

# 1D-style slicing from a flattened array
print("first 5 elements:", arr.flatten()[:5])

# 2D slices
print("first two rows:\n", arr[:2, :])
print("last two columns:\n", arr[:, 2:])
print("submatrix:\n", arr[1:, 1:3])

# slice with step
print("every second column:\n", arr[:, ::2])
print("every other row:\n", arr[::2, :])

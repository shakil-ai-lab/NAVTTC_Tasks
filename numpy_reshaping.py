import numpy as np

arr = np.arange(12)
print("original:", arr)
print("reshaped 3x4:\n", arr.reshape(3, 4))
print("flattened view:", arr.ravel())
print("flattened copy:", arr.flatten())

arr2 = np.arange(16).reshape(4, 4)
print("transposed:\n", arr2.T)
print("reshaped 2x8:\n", arr2.reshape(2, 8))
print("inferred shape 2x-1:\n", arr2.reshape(2, -1))

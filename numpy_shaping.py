import numpy as np

arr = np.arange(12)
print("shape:", arr.shape)
print("ndim:", arr.ndim)
print("size:", arr.size)
print("dtype:", arr.dtype)

arr2 = np.arange(12).reshape(3, 4)
print("arr2 shape:", arr2.shape)
print("arr2 ndim:", arr2.ndim)

# convert shape with tuple assignment
arr2.shape = (2, 6)
print("reshaped by shape assignment:\n", arr2)
print("new shape:", arr2.shape)

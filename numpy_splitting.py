import numpy as np

arr = np.arange(12).reshape(3, 4)
print("original:\n", arr)

print("split 3 arrays along columns:")
print(np.hsplit(arr, 2))

print("split 3 arrays along rows:")
print(np.vsplit(arr, 3))

print("array_split with uneven parts:")
print(np.array_split(arr, 5, axis=1))

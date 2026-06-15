import numpy as np

arr = np.arange(6)
view = arr.view()
copy = arr.copy()

print("original:", arr)
print("view:", view)
print("copy:", copy)

arr[0] = 99
print("after modify original:")
print("original:", arr)
print("view:", view)
print("copy:", copy)

print("view.base is original:", view.base is arr)
print("copy.base:", copy.base)

# Reshape returns a view when possible
arr2 = np.arange(9)
reshaped = arr2.reshape((3, 3))
print("reshaped base is arr2:", reshaped.base is arr2)

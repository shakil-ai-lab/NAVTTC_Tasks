import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2])
print("original:", arr)
print("sorted:", np.sort(arr))
print("argsort:", np.argsort(arr))

arr2 = np.array([[3, 2, 1], [6, 5, 4]])
print("sort along axis 0:\n", np.sort(arr2, axis=0))
print("sort along axis 1:\n", np.sort(arr2, axis=1))

keys = np.array([3, 1, 4])
values = np.array(['c', 'a', 'd'])
order = np.argsort(keys)
print("lexsort order:", np.lexsort((values, keys)))

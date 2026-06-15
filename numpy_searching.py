import numpy as np

arr = np.array([2, 8, 1, 6, 3, 8, 4])

print("where > 5:", np.where(arr > 5))
print("nonzero:", np.nonzero(arr))
print("argmax:", np.argmax(arr))
print("argmin:", np.argmin(arr))
print("isin [1, 4, 9]:", np.isin(arr, [1, 4, 9]))

arr2 = np.array([[1, 2, 3], [4, 2, 6]])
print("searchsorted 2 in sorted array:", np.searchsorted(np.sort(arr2.flatten()), 2))

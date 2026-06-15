import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print("concatenate axis=0:\n", np.concatenate([arr1, arr2], axis=0))
print("concatenate axis=1:\n", np.concatenate([arr1, arr2], axis=1))
print("vstack:\n", np.vstack([arr1, arr2]))
print("hstack:\n", np.hstack([arr1, arr2]))
print("stack axis=0:\n", np.stack([arr1, arr2], axis=0))
print("stack axis=1:\n", np.stack([arr1, arr2], axis=1))

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("iterate rows:")
for row in arr:
    print(row)

print("iterate elements:")
for x in np.nditer(arr):
    print(x, end=" ")
print()

print("iterate with index:")
for index, x in np.ndenumerate(arr):
    print(index, x)

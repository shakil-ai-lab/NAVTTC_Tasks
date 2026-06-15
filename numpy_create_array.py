import numpy as np

# Create arrays from Python lists
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2], [3, 4]])
print("arr1:", arr1)
print("arr2:\n", arr2)

# Create arrays using built-in NumPy methods
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)
identity = np.eye(3)

print("zeros:\n", zeros)
print("ones:\n", ones)
print("arange:", arange)
print("linspace:", linspace)
print("identity:\n", identity)

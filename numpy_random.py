import numpy as np

print("random floats:", np.random.rand(3, 2))
print("random integers:", np.random.randint(1, 10, size=(3, 3)))
print("random choice:", np.random.choice([10, 20, 30, 40], size=5))

arr = np.arange(10)
np.random.shuffle(arr)
print("shuffled:", arr)

print("normal distribution sample:", np.random.normal(loc=0.0, scale=1.0, size=5))
print("random permutation:", np.random.permutation(5))

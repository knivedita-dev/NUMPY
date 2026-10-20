# Randon Numbers (use in simulations,modelling)
import numpy as np

# rng = random numbers
rng = np.random.default_rng(seed =1)
print(rng.integers(1,7))

print(rng.integers (low=1 ,high=104, size=5))
print(rng.integers (low=1 ,high=104, size=(3,3)))

np.random.seed(seed=1)
print(np.random.uniform(low = -1 , high=1 , size=(3,2)))

# sequence to random order
rng = np.random.default_rng(seed = 1)
arr = np.array([1,3,5,7])
rng.shuffle(arr)
print(arr)
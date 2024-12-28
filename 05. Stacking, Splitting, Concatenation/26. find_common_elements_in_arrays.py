import numpy as np
a = np.random.randint(5, 20, 15)
print(a)
b = np.random.randint(2, 50, 15)
print(b)

common = np.intersect1d(a,b)
print(common)

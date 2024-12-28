import numpy as np
arr = np.random.randint(5,10,(5,3)) + np.random.random((5,3))
print(arr)
print()

arr = np.random.uniform(5,10, 15).reshape(5,-1)
print(arr)
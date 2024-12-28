import numpy as np
arr = np.arange(9).reshape(3,-1)
print(arr.shape)

print(arr)
print()

# swaping the col 3 with 2
arr = arr[:,-1:0:-1]
print(arr)
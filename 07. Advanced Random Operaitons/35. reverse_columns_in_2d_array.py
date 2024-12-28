import numpy as np

arr = np.arange(9).reshape(3,-1)
print(arr)
print()

reversed_arr = arr[:,::-1]
print(reversed_arr)
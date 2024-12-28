import numpy as np
arr = np.arange(24)
arr_2d = arr.reshape(2,-1)
print(arr_2d, arr_2d.ndim)
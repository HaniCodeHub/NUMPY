import numpy as np
arr = np.arange(20)
# arr[arr%2 != 0] = -1
# print(arr)
arr = np.where(arr%2 == 1, -1 , arr)
print(arr)
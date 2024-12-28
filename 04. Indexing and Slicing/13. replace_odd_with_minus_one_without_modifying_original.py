import numpy as np
arr = np.arange(10)
print(arr)
# self approach
# arr_rep = arr.copy()
# arr_rep[arr_rep%2 == 1] = -1
# print(arr_rep)

# best approach
arr_rep = np.where(arr%2 != 0, -1, arr)
print(arr_rep)
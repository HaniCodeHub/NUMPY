import numpy as np
# self approach
# arr_bool = np.arange(1,10).reshape(3,3).astype(bool)
# print(arr_bool)

# best approach
# arr_bool = np.full((3,3),True, dtype=bool)
# print(arr_bool)

# other way
# arr_bool = np.ones((3,3), dtype=bool)
# print(arr_bool)

# ........
arr_bool = np.zeros((3,3),dtype=bool)
arr_bool = ~(arr_bool)
print(arr_bool)
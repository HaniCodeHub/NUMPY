import numpy as np
arr = np.array([1,2,3])
# a = np.repeat(arr,3)
# b = np.tile(arr,3)
# sequence = np.concatenate([a,b])
# print(sequence)

print(np.r_[np.repeat(arr,3),np.tile(arr,3)])

import numpy as np
# self approach
# a = np.arange(5)
# b = np.arange(len(a), len(a)*2)
# ver_stacked = np.stack((a,b))
# print(a.ndim,b.ndim)
# print(ver_stacked, ver_stacked.ndim)

# best approaches
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
# print(a,"\n\n", b)
# ver_stacked = np.stack((a,b), axis = 1)
# ver_stacked = np.vstack((a,b))
# ver_stacked = np.concatenate((a,b), axis = 0)
ver_stacked = np.r_[a,b]
print(ver_stacked)
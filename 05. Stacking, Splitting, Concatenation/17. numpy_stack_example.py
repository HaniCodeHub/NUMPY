import numpy as np
# 1-D using stack function
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

arr12v = np.vstack((arr1,arr2))
arr12h = np.hstack((arr1,arr2))
print(arr12v)
print(arr12h)
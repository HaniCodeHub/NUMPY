import numpy as np

# 1-D using concatenate function
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

arr = np.concatenate((arr1,arr2))
print(arr1)
print(arr2)
print(arr)

print()

# 2-D using concatenate function
arr11 = np.array([[1,2],[3,4]])
arr22 = np.array([[9,8],[7,6]])

arr1122 = np.concatenate((arr11,arr22),axis=1)
print(arr11)
print(arr22)
print(arr1122)
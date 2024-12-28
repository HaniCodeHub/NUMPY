import numpy as np
# 1-D ARRAY
arr = np.array([1,2,3,4,5,6])
arr1 = np.array_split(arr,3)
print(arr1, type(arr1))
print(arr1[0], type(arr1[0]))

# 2-D Array
var = np.array([[1,2],[3,4],[5,6]])
var1 = np.array_split(var,3)
print()
print(var, type(var), type(var[0]))
print(var1, type(var1), type(var1[0]))
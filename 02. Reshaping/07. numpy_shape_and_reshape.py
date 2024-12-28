import numpy as np
# shape function
arr1 = np.array([[1,2,3],[1,2,3]])
print(arr1)
print(arr1.shape)
print(arr1.ndim)

print()
# reshape funtion   # 1D to 2D
arr2 = np.array([1,2,3,4,5,6])
print(arr2, arr2.ndim)
# convert 1D to 2D array
x = arr2.reshape(2,3)
print(x)
print(x.ndim)

# 1D to 3D
arr3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr3, arr3.ndim)
y = arr3.reshape(6,1,2)
print(y, y.ndim)

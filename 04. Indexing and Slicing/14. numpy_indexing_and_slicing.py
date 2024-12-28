import numpy as np
# indexing and slicing

# 1-D ARRAY
print("1-D")
arr1 = np.arange(10)
# indexing
print(arr1)
print(arr1[5])
# slicing
print(arr1[0:])
print(arr1[-1::-1])

# 2-D ARRAY
print("\n2-D")
arr2 = np.array([[1,2,3],[4,5,6]])
# indexing
print(arr2)
print(arr2[0,2])
print(arr2[1,2])
# slicing
print(arr2[0,0:])
print(arr2[1,-1::-1])

# 3-D ARRAY
print("\n3-D")
arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr3)
# indexing
print(arr3[1,1,1])
print(arr3[1,0,1])
# slicing
print(arr3[1,1,0:])
print(arr3[1,0,-1::-1])
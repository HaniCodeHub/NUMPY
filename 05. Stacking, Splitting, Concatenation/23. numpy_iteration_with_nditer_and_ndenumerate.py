import numpy as np
arr1 = np.arange(10)
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]]])

# # 1-D
# np.nditer function for iteration
print(arr1)
for i in np.nditer(arr1):
    print(i)

print("\n")
# np.ndenumerate function for indexing and element
for i,e in np.ndenumerate(arr1):
    print(i,e)

# # 2-D 
print("\nDimension", arr2.ndim)
print(arr2)
# np.nditer for iteration
for i in np.nditer(arr2):
    print(i)

print("\nindexing and element")
#np.ndenumerate function for indexing and element
for i,e in np.ndenumerate(arr2):
    print(i,e) 

# 3-D
print("\nDimension", arr3.ndim)
print(arr3)

# np.nditer function for iteration
for i in np.nditer(arr3):
    print(i)

# np.enumerate function for indexing and element
for i,e in np.ndenumerate(arr3):
    print(i,e)

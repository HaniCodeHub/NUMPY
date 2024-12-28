import numpy as np
arr1 = np.arange(10)
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]]])

# 1-D
print(arr1)
for i in arr1:
    print(i)

print("\n")
print(arr2)
# 2-D
print("iterate on each row")
for i in arr2:
    print(i)

print("iterate on each element")
for i in arr2:
    for j in i:
        print(j)

# 3-D
print("\n")
print(arr3)

print("iterate on each block")
for i in arr3:
    print(i)
print("iterate on each row")
for i in arr3:
    for j in i:
        print(j)
print("iterate on each element")
for i in arr3:
    for j in i:
        for k in j:
            print(k)
    
print("using nditer() function")
for i in np.nditer(arr3):
    print(i)
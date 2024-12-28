import numpy as np

# use of where keyword
arr = np.array([1,2,3,4,5,8])
x = np.where(arr%2 == 0)
print(x)
print(arr[x])
print()

# use of sort an array
unsorted_arr = np.array([3,2,5,6,1])
print(unsorted_arr)
sorted_arr = np.sort(unsorted_arr)
print(sorted_arr)

unsorted_str = np.array(['c','d','a','b'])
print(unsorted_str)
sorted_str = np.sort(unsorted_str)
print(sorted_str)
print()

# use of searchsorted() in array
arr2 = sorted_arr.copy()
print(arr2)
x = np.searchsorted(arr2,4)
print(x)
print()

# use of filter in numpy
arr_str2 = unsorted_str
print(arr_str2)
f = [True,False,False,True]
print(arr_str2[f])

print()

var = np.array([1,2,3,4])
index = [1,3]
print(var[var-len(arr)+2])

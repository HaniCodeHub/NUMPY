import numpy as np
# arithematic operations
# for 1D ARRAY...................................
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
# addition and sub are same
# add_arr = arr1 + arr2
add_arr = np.add(arr1,arr2)
print(add_arr)

# multiply and divide are same
# mul_arr = arr1 * arr2
mul_arr = np.multiply(arr1, arr2)
print(mul_arr)

# mod
# mod_arr = arr1 % 3
mod_arr = np.mod(arr1, 3)
print(mod_arr)

# FOR 2D ARRAY
arr1 = np.array([[1,2,3],[1,2,3]])
arr2 = np.array([[1,2,3],[1,2,3]])

arr_add = np.add(arr1, arr2)
print(arr_add)

# basic arithmatic function..........................
# min / max and agrmin/max
print(arr1)
min_arr = np.min(arr1)
print(f"{min_arr} at index {np.argmin(arr1)}")
max_arr = np.max(arr1)
print(f"{max_arr} at index {np.argmax(arr1)}")


# sqrt
arr11 = np.array([9, 4, 16])
sqrt_arr = np.sqrt(arr11)
sqrt_arr = sqrt_arr.astype(int)
print(sqrt_arr)

# sin cos
sin_arr = np.sin(arr11)
cos_arr = np.cos(arr11)
print(sin_arr)
print(cos_arr)

# cumsum function
series = np.arange(10)
sum_series = np.cumsum(series)
print(sum_series)

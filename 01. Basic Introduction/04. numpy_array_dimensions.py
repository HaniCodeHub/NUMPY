import numpy as np
list = [1,2,3,4]
one_d_arr = np.array(list)
print(one_d_arr)
print(one_d_arr.ndim)

two_d_arr = np.array([list])
print(two_d_arr)
print(two_d_arr.ndim)

three_d_arr = np.array([[list]])
print(three_d_arr)
print(three_d_arr.ndim)

# multi-dimensional array
# create a multi_dimensional array using the following code
mul_d_arr = np.array(list, ndmin = 10)
print(mul_d_arr)
print(mul_d_arr.ndim)

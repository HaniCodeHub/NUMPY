import numpy as np
# a = np.arange(10)
# b = np.arange(1,20,2)
# print(a.shape, b.shape)
# # max_no = np.max((a,b),axis = 0)
# # if we want to get only one max element then 
# c = np.hstack((a,b))
# print(c)
# max_no = np.max(c)
# print(max_no)

# using the user defined functions
def max_no(x,y):
    if x>=y:
        return x
    else:
        return y

num = np.vectorize(max_no, otypes=[int])
a,b = np.arange(10),np.arange(1,20,2)
print(num(a,b))

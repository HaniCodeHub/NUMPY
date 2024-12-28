import numpy as np
arr = np.array([1,2,3,4])
# copy
cpy = arr.copy()
# view
vw = arr.view()
print("without any change")
print("original: ", arr)
print("copied: ", cpy)
print("viewed: ", vw)
print()

# made changes the original array then print
print("changes in original array")
arr[1] = 40
print("original: ", arr)
print("copied: ", cpy)
print("viewed: ", vw)
print()

# changes made in copy and then print them
print("changes made in copy array")
cpy[3] = 44
print("original: ", arr)
print("copied: ", cpy)
print("viewed: ", vw)
print()

# changes made in view and then print them
print("changes made in view array")
vw[3] = 33
print("original: ", arr)
print("copied: ", cpy)
print("viewed: ", vw)


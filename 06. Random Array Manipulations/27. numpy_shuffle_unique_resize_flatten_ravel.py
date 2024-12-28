import numpy as np
# shuffle
arr = np.arange(10)
print(arr)
np.random.shuffle(arr)
print(arr)
print()

# unique 
arr = np.array([1,2,4,51,2,4,5,6,2,3,4,6])
u = np.unique(arr,return_index=True,return_counts=True)
print(arr)
print(u)
print()

# Resize
arr = np.arange(6)
print(arr)
r = np.resize(arr,(3,2))
print(r)
print()

# Flatten and ravel
print(r.flatten())
print(r.flatten(order="F"))
print(r)
print()

print(np.ravel(r))
print(np.ravel(r,order="F"))
import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.full((2,5),5)
print(a,"\n",b)

print()

hor_stacked = np.concatenate([a,b],axis = 1)
print(hor_stacked)

print()

hor_stacked = np.hstack([a,b])
print(hor_stacked)

print()

hor_stacked = np.c_[a,b]
print(hor_stacked)

print(np.info(np.concatenate))
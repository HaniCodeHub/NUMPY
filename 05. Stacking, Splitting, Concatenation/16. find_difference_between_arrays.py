import numpy as np
a = np.arange(10)
b = np.arange(1, 20, 2)
# print(a.shape, b.shape)
print(a,"\n", b)
differ = np.setdiff1d(a,b)
print()
print(differ)
# print(np.info(np.diff))

import numpy as np
a = np.arange(20)
# num = np.where((a>=5) & (a<11))
# num = np.logical_and((a>4),(a<11))

# print(a[num])

# other way
print(a[(a>4)&(a<11)])

import numpy as np

# Array filled with 0's
ar_zero = np.zeros(4, dtype = np.int8)
print((ar_zero))
print()

# Array filled with 1's
ar_one = np.ones(4, dtype = np.int8)
print(ar_one)
print()

# Create an empty array
ar_em = np.empty(4, dtype = np.int8)
print(ar_em)
print()

# An array with a range of elements
ar_rn = np.arange(5)
print(ar_rn)
print()

# Array diagonal element filled with 1's
ar_dia = np.eye(3, dtype = np.int8)
print(ar_dia)
print()

# Create an array with values that are spaced linearly in a specified interval.
ar_interval = np.linspace(0, 10, 5, dtype = np.int8)
print(ar_interval)
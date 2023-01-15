import numpy as np

# 一维
x1 = np.zeros(5, dtype=float)
print(x1, type(x1), x1.dtype)

x2 = np.ones(5, dtype=float)
print(x2, type(x2), x2.dtype)

x3 = np.empty(6, dtype=float)
print(x3, type(x3), x3.dtype)

# 多维
x1 = np.zeros((5, 2), dtype=float)
print(x1, type(x1), x1.dtype)

x2 = np.ones((5, 2), dtype=float)
print(x2, type(x2), x2.dtype)

x3 = np.empty((5, 2), dtype=float)
print(x3, type(x3), x3.dtype)

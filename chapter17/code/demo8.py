import numpy as np

# 一维
x1 = np.arange(10, dtype=np.float32)
print(x1, type(x1), x1.dtype)
x2 = np.arange(2, 10)
x3 = np.arange(2, 3, 0.1)
print(x3, type(x3), x3.dtype)

# 多维
x4 = np.arange(10).reshape(2,5)
print(x4, type(x4), x4.dtype)



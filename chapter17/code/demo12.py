import numpy as np

x = np.arange(12).reshape(3, 4)


# print(x)
# print(x[0])
# print(x[:, 1], type(x[:, 1]))
# print(x[0:2, 0:2])

def f(x, y):
    return x + y


x2 = np.fromfunction(f, (3, 2), dtype=int)
print(x2)
"""
x = [[0 0]
 [1 1]
 [2 2]]
y = [[0 1]
 [0 1]
 [0 1]]
"""

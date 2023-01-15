import numpy as np

x = np.arange(5)
print(x, x.shape)

y = np.arange(15).reshape(3, 5)
print(y, y.shape)

print(x+y)
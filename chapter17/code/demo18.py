import numpy as np

x = np.arange(3).reshape(3,1)
print(x, x.shape)

y = np.arange(5).reshape(1, 5)
print(y, y.shape)

print(x+y)
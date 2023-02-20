import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(50)
y = np.random.randn(50)
print(x)
print(y)
plt.scatter(x, y, cmap='twilight')

plt.show()

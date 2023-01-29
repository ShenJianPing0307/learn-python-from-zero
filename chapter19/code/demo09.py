import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2, 100)
y1 = x ** 3
y2 = x

plt.style.use("bmh")

# 颜色使用[0,1]之间的浮点数表示(red, green, blue, alpha)
plt.plot(x, y1, color=(0.1, 0.2, 0.5))
plt.plot(x, y2, color=(0.1, 0.2, 0.5, 0.5))

plt.show()

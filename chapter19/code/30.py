import matplotlib.pyplot as plt
import numpy as np

# 用fill来绘制图形
x = np.linspace(0, 5 * np.pi, 1000)
y = np.sin(x)
plt.fill(x, y, color = "g", alpha = 0.3)
plt.show()

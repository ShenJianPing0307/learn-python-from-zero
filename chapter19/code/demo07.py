import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2, 100)
y = x ** 3

plt.style.use("file/pre.mplstyle")
# plt.style.use(["default", "file/pre.mplstyle"])

plt.plot(x, y)

plt.show()

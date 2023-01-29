import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2, 100)
y = x ** 3

plt.style.use("bmh")

plt.plot(x, y)

plt.show()

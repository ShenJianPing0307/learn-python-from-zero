import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()
ax.plot(x, x**3)
ax.plot(x, x**2)

plt.show()
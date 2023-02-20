import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

x = np.arange(10)
y1 = x**2
y2 = x**3

fig, ax = plt.subplots()

ax.plot(x, y1)
ax.plot(x, y2)

print(ax.lines[0])

plt.show()
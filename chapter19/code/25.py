import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

x = np.arange(10)
y1 = x ** 2
y2 = x ** 3

fig, ax = plt.subplots()

lines = [Line2D(x, y1), Line2D(x, y2, color="orange")]

for line in lines:
    ax.add_line(line)

print(type(ax))
plt.show()

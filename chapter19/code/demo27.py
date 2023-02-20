# Rectangle矩形类绘制直方图
from matplotlib import pyplot as plt
import numpy as np
import random

fig = plt.figure()
ax1 = fig.add_subplot()

for i in np.arange(0, 101, 10):
    rect = plt.Rectangle((i, 0), 10, random.randint(0, 100))
    ax1.add_patch(rect)

ax1.set_xlim(0, 100)
ax1.set_ylim(0, 16);
plt.show()
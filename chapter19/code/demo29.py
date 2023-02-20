import matplotlib.pyplot as plt
import numpy as np

# Rectangle矩形类绘制柱状图
fig = plt.figure()
ax1 = fig.add_subplot()

for i in range(1, 17):
    rect = plt.Rectangle((i + 0.25, 0), 0.5, i)
    ax1.add_patch(rect)
ax1.set_xlim(0, 16)
ax1.set_ylim(0, 16)

plt.show()

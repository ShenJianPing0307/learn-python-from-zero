import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

# 1、准备数据
x = np.linspace(0, 2, 100)
y1 = x ** 2
y2 = x ** 3

# 2、设置绘图的样式
mpl.rc('lines', linewidth=5, linestyle='-.')

# 3、定义布局
fig, ax = plt.subplots()

# 4、绘制图像
ax.plot(x, y1, label="liner1")
ax.plot(x, y2, label="liner2")

# 5、标签、文字、图例
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title('simple line')
ax.legend()

# 6、显示图像
plt.show()

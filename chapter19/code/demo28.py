import matplotlib.pyplot as plt
import numpy as np

# bar绘制柱状图
y = range(1,17)
plt.bar(np.arange(16), y, alpha=0.5, width=0.8, color='yellow', edgecolor='red', label='The First Bar', lw=3);
plt.show()
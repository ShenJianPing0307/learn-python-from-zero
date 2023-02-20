import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)


fig, ax = plt.subplots(1, 3)

for i in range(3):
    ax[i].plot(x, x**i)
    # 位置
    ax[i].legend(labels=f'l{i}', title='title', loc=2, frameon=True, edgecolor='blue', facecolor='green')  # loc='upper right'


plt.show()
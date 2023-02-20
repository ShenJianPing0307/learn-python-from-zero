import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2, 5)

for i in range(2):
    for j in range(5):

        ax[i][j].scatter(np.random.randn(10), np.random.randn(10))

plt.show()
import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0, 0.5, 100)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)

fig, ax = plt.subplots(2, 1, figsize=(5, 3), tight_layout=True)

ax[0].plot(x1, y1)

ax[1].plot(x1, y1)
ax[1].xaxis.set_ticks(np.arange(0, 10.1, 2))
ax[1].yaxis.set_ticks(np.arange(0, 10.1, 2))

tickla = [f'{tick:1.2f}' for tick in np.arange(0, 10.1, 2)]
ax[1].xaxis.set_ticklabels(tickla, rotation=30)

plt.show()
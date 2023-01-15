import numpy as np

# print(np.sin(np.pi/2))
#
# print(np.sin(np.array((30, 60, 90))*np.pi / 180))

import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x))
plt.show()
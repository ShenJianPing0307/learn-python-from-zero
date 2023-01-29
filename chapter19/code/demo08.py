import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2, 100)
y = x ** 3

print(mpl.rcParams)
mpl.rcParams['lines.linewidth'] = 2 #  rc('lines', linewidth=2, color='r')

plt.plot(x, y)

plt.show()
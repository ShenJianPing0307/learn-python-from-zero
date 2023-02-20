import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot()
ax2 = fig.add_subplot()

ax1.plot()
ax2.hist()

print(fig.axes)
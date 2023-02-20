import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = range(0, 5)
y = range(5, 10)

plt.plot(x, y)

ax.yaxis.set_tick_params(labelleft=False, labelright=True)

plt.show()

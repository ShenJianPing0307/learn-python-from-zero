import matplotlib.pyplot as plt

fig, ax =  plt.subplots()
x = range(0, 5)
y = range(5, 10)

plt.plot(x, y)

axis = ax.xaxis
print(axis.get_ticklocs())
print(axis.get_ticklabels())
print(axis.get_data_interval())

for label in axis.get_ticklabels():
    label.set_color('red')
    label.set_rotation(45)
    label.set_fontsize(16)

plt.show()
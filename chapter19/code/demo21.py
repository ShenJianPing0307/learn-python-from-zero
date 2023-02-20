import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

# 设置标题
fig.suptitle("figure title", fontsize=14, fontweight="bold")
ax.set_title("axes title")

# 在figure上添加文本
fig.text(0.5, 0.8, 'fig text content！')

# 设置x、y轴标签
ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")

# 设置x、y轴显示范围[0,10]
ax.axis([0, 10, 0, 10])

# 在ax上添加文本
ax.text(3, 8, 'ax text content！', bbox={'alpha': 0.5, 'pad': 10})

ax.plot([1, 2, 3], [1, 2, 3])

plt.show()

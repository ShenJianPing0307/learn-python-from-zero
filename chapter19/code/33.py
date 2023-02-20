import matplotlib.pyplot as plt


# 用scatter绘制散点图
x = [0,2,4,6,8,10]
y = [10]*len(x)
s = [20*2**n for n in range(len(x))]
plt.scatter(x,y,s=s) # s尺寸大小
plt.show()
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']   #用来正常显示中文标签

# hist绘制直方图
x=np.random.randint(0,100,100) #生成[0-100)之间的100个数据,即 数据集
bins=np.arange(0,101,10) #设置连续的边界值，即直方图的分布区间[0,10),[10,20)...

plt.hist(x,bins,color='fuchsia',alpha=0.5, align='left')#alpha设置透明度，0为完全透明

plt.xlabel('分数')
plt.ylabel('个数')
plt.xlim(0,100); #设置x轴分布范围

plt.show()

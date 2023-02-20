import seaborn as sns
import matplotlib.pyplot as plt

# 设置主题样式
sns.set_theme()

# 加载数据集
tips = sns.load_dataset("tips")
print(tips, type(tips))

sns.relplot(data=tips, x="total_bill", y="tip")

plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
g = sns.relplot(data=flights, x="year", y="passengers", kind="line", hue="month")
g.savefig('demo22') # 路径
plt.savefig('demo221.png')
# plt.show()
from seaborn.axisgrid import FacetGrid
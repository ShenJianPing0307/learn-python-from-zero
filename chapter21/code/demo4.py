import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")
sns.lineplot(data=tips, x="total_bill", y="tip")

plt.show()
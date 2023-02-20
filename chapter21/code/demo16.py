import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips)
sns.catplot(data=tips, x="day", y="total_bill", kind="point")

plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.catplot(data=tips, x="day", y="total_bill", kind="bar")

plt.show()
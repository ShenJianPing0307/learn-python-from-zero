import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
sns.relplot(data=flights, x="year", y="passengers", kind="line", hue="month")

plt.show()
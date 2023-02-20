import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
print(penguins)
print(penguins.columns)
sns.relplot(penguins, x='bill_length_mm', y='bill_depth_mm')
sns.rugplot(penguins, x='bill_length_mm', y='bill_depth_mm')

plt.show()


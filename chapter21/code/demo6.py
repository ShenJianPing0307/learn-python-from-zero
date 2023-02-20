import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
print(penguins)

sns.displot(penguins, x='flipper_length_mm', kind='kde', multiple='stack')

plt.show()


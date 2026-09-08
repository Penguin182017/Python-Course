import seaborn as sns
import matplotlib.pyplot as plt

names = ["Kiko", "Bobo", "Ice"]
weights = [12, 15, 10]

sns.barplot(x=names, y=weights)

plt.show()
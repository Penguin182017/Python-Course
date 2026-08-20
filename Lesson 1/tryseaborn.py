import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

penguins = ['Pip', 'Bobo', 'Kiko', 'Pingu', 'Snowy', 'Ice']
weight = [3.2, 4.1, 5.0, 3.8, 4.5, 5.3]
flipper = [180, 190, 205, 185, 198, 215]
species = ['Small', 'Medium', 'Large',
           'Small', 'Medium', 'Large']

# scatter plot
sns.scatterplot(x=weight, y=flipper, hue=species)
plt.title("Penguin Size Groups")
plt.xlabel("Weight (kg)")
plt.ylabel('Flipper Length (mm)')
plt.grid(True)
plt.ylim(170, 220)
plt.show()

penguins = ['Pip', 'Bobo', 'Kiko']
fish = [12, 8, 15]

# bar plot
sns.barplot(x=penguins, y=fish)

plt.xlabel("Penguins")
plt.ylabel("Fish")
plt.show()

penguins = ['Pip', 'Bobo', 'Kiko']
fish = [12, 8, 15]

sns.barplot(x=penguins, y=fish, linewidth=5)

plt.title("Penguin Fish Challenge")
plt.xlabel("Penguins")
plt.ylabel("Fish")
plt.ylim(0, 15)

plt.show()

penguins = ['Pip', 'Bobo', 'Kiko']
fish = [12, 8, 15]

sns.barplot(
    x=penguins,
    y=fish,
    linewidth=3,
    color='orange'
)

plt.title("Penguin Fish Challenge")
plt.xlabel("Penguins")
plt.ylabel("Fish Caught")
plt.ylim(0, 20)

plt.show()

penguins = ['Pip', 'Pip', 'Bobo', 'Bobo', 'Kiko', 'Kiko']

day = [1, 2, 1, 2, 1, 2]

fish = [5, 12, 3, 8, 7, 15]

sns.barplot(
    x=penguins,
    y=fish,
    hue=day,
    linewidth=3,
    color='orange'
)

plt.title("Penguin Fish Challenge")
plt.xlabel("Penguins")
plt.ylabel("Fish Caught")
plt.ylim(0, 20)
plt.legend(title='Fishing Day')

plt.show()

penguins = ['Pip', 'Pip', 'Pip',
            'Bobo', 'Bobo', 'Bobo',
            'Kiko', 'Kiko', 'Kiko']

day = [1, 2, 3,
       1, 2, 3,
       1, 2, 3]

fish = [5, 12, 9,
        3, 8, 11,
        7, 15, 13]

sns.barplot(
    x=penguins,
    y=fish,
    hue=day,
    linewidth=2
)

plt.title("Penguin Fishing Report")
plt.xlabel("Penguins")
plt.ylabel("Fish Caught")
plt.ylim(0, 20)
plt.legend(title='Fishing Day')

plt.show()

penguins = ['Pip', 'Bobo', 'Kiko', 'Pingu', 'Snowy', 'Ice']

weight = [3.2, 4.1, 5.0, 3.8, 4.5, 5.3]

flipper = [180, 190, 205, 185, 198, 215]

# scatter plot
sns.scatterplot(
    x=weight,
    y=flipper,
    hue=penguins
)

plt.title("Penguin Size Detective")
plt.xlabel("Weight (kg)")
plt.ylabel("Flipper Length (mm)")
plt.ylim(170, 220)

plt.show()

penguins = ['Pip', 'Bobo', 'Kiko', 'Pingu', 'Snowy', 'Ice']

weight = [3.2, 4.1, 5.0, 3.8, 4.5, 5.3]

flipper = [180, 190, 205, 185, 198, 215]

# reg plot
sns.regplot(x=weight, y=flipper)

plt.title("Penguin Weight vs Flipper Length")
plt.xlabel("Weight (kg)")
plt.ylabel("Flipper Length (mm)")
plt.grid(True)
plt.ylim(170, 220)

plt.show()

# heatmap
data = {
    'Weight': [3.2, 4.1, 5.0, 3.8, 4.5, 5.3],
    'Flipper': [180, 190, 205, 185, 198, 215],
    'Age': [2, 3, 5, 3 , 4, 6], 
    'Swimming': [70, 80, 95, 75, 88, 100]
}
df = pd.DataFrame(data)
correlation = df.corr()
sns.heatmap(correlation, annot=False, linewidth=1)
plt.title('🐧 Advanced Penguin Analysis')
plt.show()

data = {
    'Name': ['Pip', 'Bobo', 'Kiko', 'Pingu', 'Snowy', 'Ice'],
    'Weight': [3.2, 4.1, 5.0, 3.8, 4.5, 5.3],
    'Flipper': [180, 190, 205, 185, 198, 215],
    'Age': [2, 3, 5, 3 , 4, 6]
}
df = pd.DataFrame(data)

# pair plot
sns.pairplot(df, kind='reg')

plt.show()

#box plot
sns.boxplot(
    data=df,
    x='Age',
    y='Weight'
)

plt.show()

# violin plot
sns.violinplot(
    data=df,
    x='Age',
    y='Weight'
)
plt.show()

# joint plot
sns.jointplot(
    data=df,
    x='Weight',
    y='Flipper',
    kind='kde'
)

plt.show()

fig, axes = plt.subplots(2, 2)

sns.scatterplot(data=df, x='Weight', y='Flipper', ax=axes[0, 0])

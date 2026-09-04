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


# 3 plots
fig, axes = plt.subplots(1, 3)

sns.scatterplot(data=df, x='Weight', y='Flipper', ax=axes[0])
sns.boxplot(data=df, x='Age', y='Weight', ax=axes[1])
sns.histplot(data=df, x='Weight', ax=axes[2])

plt.tight_layout()
plt.show()


#🤷‍♂️
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    df['Age'],
    df['Weight'],
    df['Flipper']
)

ax.set_xlabel('Weight')
ax.set_ylabel('Flipper')
ax.set_zlabel('Age')

plt.show()

#surface plot
import numpy as np
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)

Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()


#plotly
import plotly.express as px

fig = px.scatter_3d(
    df,
    x='Age',
    y='Weight',
    z='Flipper',
    text='Name'
)

fig.show()



fig = px.scatter(
    df,
    x='Weight',
    y='Flipper',
    hover_name='Name',
    hover_data=['Age'],
    title='🐧 Penguin Weight vs Flipper'
)

fig.show()


import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Weight'],
    y=df['Flipper'],
    mode='markers',
    name='Penguins'
))

fig.update_layout(
    title='🐧 Penguin Explorer',
    xaxis_title='Weight',
    yaxis_title='Flipper',
    updatemenus=[{
        'buttons': [
            {
                'label': 'Weight',
                'method': 'update',
                'args': [{'x': [df['Weight']]},
                        {'xaxis': {'title': 'Weight'}}]
            },
            {
                'label': 'Age',
                'method': 'update',
                'args': [{'x': [df['Age']]},
                        {'xaxis': {'title': 'Age'}}]
            }
        ]
    }]
)

fig.show()


import pandas as pd
import plotly.express as px

data = {
    'Name': [
        'Pip', 'Bobo', 'Kiko', 'Pingu', 'Snowy', 'Ice',
        'Pip', 'Bobo', 'Kiko', 'Pingu', 'Snowy', 'Ice',
        'Pip', 'Bobo', 'Kiko', 'Pingu', 'Snowy', 'Ice'
    ],

    'Year': [
        2020, 2020, 2020, 2020, 2020, 2020,
        2021, 2021, 2021, 2021, 2021, 2021,
        2022, 2022, 2022, 2022, 2022, 2022
    ],

    'Weight': [
        2.5, 3.0, 3.5, 2.8, 3.2, 3.7,
        2.9, 3.4, 4.0, 3.2, 3.6, 4.2,
        3.4, 3.9, 4.5, 3.7, 4.1, 4.7
    ],

    'Flipper': [
        160, 165, 170, 162, 168, 172,
        170, 175, 182, 173, 178, 185,
        178, 183, 190, 181, 187, 193
    ]
}

df = pd.DataFrame(data)

fig = px.scatter(
    df,
    x='Weight',
    y='Flipper',
    animation_frame='Year',
    animation_group='Name',
    text='Name',
    size='Weight',
    range_x=[2, 5],
    range_y=[155, 200],
    title='🐧 Penguin Growth'
)

fig.show()

import plotly.express as px

df = px.data.gapminder()

fig = px.choropleth(
    df,
    locations='iso_alpha',
    color='gdpPercap',
    hover_name='country',
    animation_frame='year',
    color_continuous_scale='Viridis',
    title='🌍 GDP Around the World'
)

fig.show()


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

data = {
    'Name': ['Pip', 'Bobo', 'Kiko', 'Pingu', 'Snowy', 'Ice'],
    'Weight': [3.2, 4.1, 5.0, 3.8, 4.5, 5.3],
    'Flipper': [180, 190, 205, 185, 198, 215],
    'Age': [2, 3, 5, 3, 4, 6]
}

df = pd.DataFrame(data)

app = Dash(__name__)

fig1 = px.scatter(
    df,
    x='Weight',
    y='Flipper',
    text='Name',
    title='🐧 Weight vs Flipper'
)

fig2 = px.bar(
    df,
    x='Name',
    y='Weight',
    title='🐧 Penguin Weight'
)

app.layout = html.Div([
    html.H1('🐧 Penguin Data Dashboard'),

    dcc.Graph(figure=fig1),

    dcc.Graph(figure=fig2)
])

app.run(debug=True)
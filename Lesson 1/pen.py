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
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# ---------------- DATA ----------------

data = {
    "Name": [
        "Pip", "Pip", "Pip", "Pip",
        "Bobo", "Bobo", "Bobo", "Bobo",
        "Kiko", "Kiko", "Kiko", "Kiko",
        "Pingu", "Pingu", "Pingu", "Pingu",
        "Snowy", "Snowy", "Snowy", "Snowy",
        "Ice", "Ice", "Ice", "Ice"
    ],

    "Year": [
        2020, 2021, 2022, 2023,
        2020, 2021, 2022, 2023,
        2020, 2021, 2022, 2023,
        2020, 2021, 2022, 2023,
        2020, 2021, 2022, 2023,
        2020, 2021, 2022, 2023
    ],

    "Weight": [
        2.5, 3.0, 3.6, 4.1,
        3.0, 3.4, 3.9, 4.3,
        3.5, 4.0, 4.5, 5.0,
        2.8, 3.2, 3.7, 4.1,
        3.2, 3.6, 4.1, 4.5,
        3.7, 4.2, 4.7, 5.2
    ],

    "Flipper": [
        160, 170, 178, 183,
        165, 174, 181, 187,
        170, 180, 188, 195,
        162, 172, 180, 186,
        168, 178, 187, 193,
        172, 183, 191, 198
    ],

    "Age": [
        1, 2, 3, 4,
        1, 2, 3, 4,
        1, 2, 3, 4,
        1, 2, 3, 4,
        1, 2, 3, 4,
        1, 2, 3, 4
    ]
}

df = pd.DataFrame(data)

# ---------------- DASH APP ----------------

app = Dash(__name__)

app.layout = html.Div([

    html.H1("🐧 Penguin Data Explorer"),

    html.H3("Choose a penguin:"),

    dcc.Dropdown(
        id="penguin-dropdown",
        options=[
            {"label": name, "value": name}
            for name in df["Name"].unique()
        ],
        value="Pip"
    ),

    html.Br(),

    html.Div(id="statistics"),

    dcc.Graph(id="weight-graph"),

    dcc.Graph(id="flipper-graph"),

    html.H2("🎬 All Penguins Growing"),

    dcc.Graph(
        figure=px.scatter(
            df,
            x="Weight",
            y="Flipper",
            animation_frame="Year",
            animation_group="Name",
            color="Name",
            text="Name",
            size="Weight",
            range_x=[2, 5.5],
            range_y=[155, 205],
            title="🐧 Penguin Growth Animation"
        )
    )
])


# ---------------- DROPDOWN UPDATE ----------------

@app.callback(
    Output("statistics", "children"),
    Output("weight-graph", "figure"),
    Output("flipper-graph", "figure"),
    Input("penguin-dropdown", "value")
)

def update_dashboard(penguin):

    selected = df[df["Name"] == penguin]

    latest = selected.iloc[-1]

    statistics = html.Div([
        html.H2(f"🐧 {penguin}"),
        html.P(f"Age: {latest['Age']} years"),
        html.P(f"Weight: {latest['Weight']} kg"),
        html.P(f"Flipper: {latest['Flipper']} mm")
    ])

    weight_fig = px.line(
        selected,
        x="Year",
        y="Weight",
        markers=True,
        title=f"{penguin}'s Weight Growth"
    )

    flipper_fig = px.line(
        selected,
        x="Year",
        y="Flipper",
        markers=True,
        title=f"{penguin}'s Flipper Growth"
    )

    return statistics, weight_fig, flipper_fig


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)
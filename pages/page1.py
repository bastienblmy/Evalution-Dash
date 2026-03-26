import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path="/", name="Comparaison entre région")

# Lecture du fichier CSV
df = pd.read_csv("datas/avocado.csv")

# Conversion et nettoyage
df["Date"] = pd.to_datetime(df["Date"])
df["region"] = df["region"].astype(str).str.strip()

# Régions imposées pour le premier graphique
regions_fixes = ["Midsouth", "Northeast", "SouthCentral", "Southeast", "TotalUS", "West"]

# Données du graphique de gauche : une valeur par date et par région
df_left = (
    df[df["region"].isin(regions_fixes)]
    .groupby(["Date", "region"], as_index=False)["Total Volume"]
    .sum()
    .sort_values("Date")
)

fig_left = px.line(
    df_left,
    x="Date",
    y="Total Volume",
    color="region",
    title="Quantités vendues - Régions principales"
)

# Options du menu déroulant
all_regions = sorted(df["region"].dropna().unique())

# Région par défaut pour le graphique de droite
default_region = all_regions[0]

# Données du graphique de droite : une valeur par date pour la région choisie
df_right = (
    df[df["region"] == default_region]
    .groupby("Date", as_index=False)["Total Volume"]
    .sum()
    .sort_values("Date")
)

fig_right = px.line(
    df_right,
    x="Date",
    y="Total Volume",
    title=f"Quantités vendues - {default_region}"
)

layout = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    html.H3("Quantités vendues (Total Volume)", className="mb-0"),
                ),
                dbc.CardBody(
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Graph(
                                    id="graph-left",
                                    figure=fig_left
                                ),
                                xs=12, md=6
                            ),
                            dbc.Col(
                                [
                                    dbc.Badge(
                                        "Sélectionnez une région :",
                                        color="primary",
                                        className="mb-3 p-2 w-100"
                                    ),
                                    dcc.Dropdown(
                                        id="region-select",
                                        options=[{"label": region, "value": region} for region in all_regions],
                                        value=default_region,
                                        clearable=False,
                                        className="mb-3"
                                    ),
                                    dcc.Graph(
                                        id="graph-right",
                                        figure=fig_right
                                    )
                                ],
                                xs=12, md=6
                            )
                        ],
                        className="g-3"
                    )
                )
            ],
            className="shadow"
        )
    ],
    fluid=True,
    className="mt-4"
)

# Met à jour le graphique de droite selon la région choisie

@callback(
    Output("graph-right", "figure"),
    Input("region-select", "value")
)
def update_graph_right(selected_region):
    df_filtered = (
        df[df["region"] == selected_region]
        .groupby("Date", as_index=False)["Total Volume"]
        .sum()
        .sort_values("Date")
    )

    fig = px.line(
        df_filtered,
        x="Date",
        y="Total Volume",
        title=f"Quantités vendues - {selected_region}"
    )

    return fig
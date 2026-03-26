from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

# Lecture des données
df = pd.read_csv("datas/avocado.csv")
df["region"] = df["region"].astype(str).str.strip()
df["type"] = df["type"].astype(str).str.strip()

# Options sans doublon
regions = sorted(df["region"].dropna().unique())
types_avocat = sorted(df["type"].dropna().unique())

# Valeurs par défaut pour le layout
default_region = regions[0]
default_type = "Tous"

# Colonnes à masquer
hidden_columns = [
    "Unnamed: 0",
    "4046",
    "4225",
    "4770",
    "Small Bags",
    "Large Bags",
    "XLarge Bags"
]

# Données affichées au départ : région par défaut, tous les types
df_display = df[df["region"] == default_region].copy()

# Colonnes visibles
visible_columns = [col for col in df_display.columns if col not in hidden_columns]

layout = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("Sélectionner une région :", className="text-white mb-2"),
                                        dcc.Dropdown(
                                            id="page2-region-dropdown",
                                            options=[{"label": r, "value": r} for r in regions],
                                            value=default_region,
                                            clearable=False
                                        ),
                                    ],
                                    xs=12, md=5
                                ),
                                dbc.Col(
                                    [
                                        html.Label("Sélectionner un type :", className="text-white mb-2"),
                                        dbc.RadioItems(
                                            id="page2-type-radio",
                                            options=[{"label": "Tous", "value": "Tous"}] +
                                                    [{"label": t, "value": t} for t in types_avocat],
                                            value=default_type,
                                            inline=True,
                                            className="text-white"
                                        ),
                                    ],
                                    xs=12, md=5
                                ),
                                dbc.Col(
                                    [
                                        html.Label(" ", className="mb-2 d-block"),
                                        dbc.Badge(
                                            f"Lignes: {len(df_display)}",
                                            id="page2-badge",
                                            color="primary",
                                            className="p-2"
                                        ),
                                    ],
                                    xs=12, md=2,
                                    className="d-flex align-items-end"
                                ),
                            ],
                            className="g-3 mb-3"
                        ),
                        html.Div(
                            dash_table.DataTable(
                                id="page2-table",
                                columns=[{"name": col, "id": col} for col in visible_columns],
                                data=df_display[visible_columns].to_dict("records"),
                                sort_action="native",
                                page_size=10,
                                style_table={"overflowX": "auto"},
                                style_cell={
                                    "textAlign": "left",
                                    "padding": "8px",
                                    "fontSize": "13px"
                                },
                                style_header={
                                    "backgroundColor": "#f0f0f0",
                                    "fontWeight": "bold"
                                }
                            ),
                            style={
                                "backgroundImage": "linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), url('/assets/BG.jpg')",
                                "backgroundSize": "cover",
                                "backgroundPosition": "center",
                                "backgroundRepeat": "no-repeat",
                                "padding": "10px",
                                "borderRadius": "4px",
                                "minHeight": "500px"
                            }
                        )
                    ]
                )
            ],
            className="shadow",
            style={"backgroundColor": "#1f1f1f"}
        )
    ],
    fluid=True,
    className="mt-4"
)
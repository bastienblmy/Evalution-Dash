import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/page3", name="Aide en ligne")

# Lecture des fichiers markdown
with open("datas/expli1.md", "r", encoding="utf-8") as f:
    content1 = f.read()

with open("datas/expli2.md", "r", encoding="utf-8") as f:
    content2 = f.read()

with open("datas/expli3.md", "r", encoding="utf-8") as f:
    content3 = f.read()

tab_style = {
    "backgroundColor": "#1f1f1f",
    "color": "#d9d9d9",
    "border": "none",
    "padding": "10px 18px",
    "fontWeight": "500"
}

tab_selected_style = {
    "backgroundColor": "#2da6df",
    "color": "white",
    "border": "none",
    "padding": "10px 18px",
    "fontWeight": "600"
}

content_style = {
    "backgroundColor": "#1f1f1f",
    "color": "white",
    "padding": "20px",
    "minHeight": "500px",
    "borderRadius": "0 0 4px 4px"
}

layout = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    html.H3("Présentation de Dash", className="mb-0 text-white"),
                    style={"backgroundColor": "#2da6df"}
                ),
                dbc.CardBody(
                    html.Div(
                        dcc.Tabs(
                            children=[
                                dcc.Tab(
                                    label="Accueil",
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.Div(
                                            dcc.Markdown(content1, style={"color": "white"}),
                                            style=content_style
                                        )
                                    ]
                                ),
                                dcc.Tab(
                                    label="Layout",
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.Div(
                                            dcc.Markdown(content2, style={"color": "white"}),
                                            style=content_style
                                        )
                                    ]
                                ),
                                dcc.Tab(
                                    label="CallBack",
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.Div(
                                            dcc.Markdown(content3, style={"color": "white"}),
                                            style=content_style
                                        )
                                    ]
                                ),
                            ],
                            colors={
                                "border": "#1f1f1f",
                                "primary": "#2da6df",
                                "background": "#1f1f1f"
                            }
                        ),
                        style={
                            "backgroundColor": "#1f1f1f",
                            "borderRadius": "4px",
                            "overflow": "hidden"
                        }
                    ),
                    style={
                        "backgroundImage": "linear-gradient(rgba(255,255,255,0.82), rgba(255,255,255,0.82)), url('/assets/BG.jpg')",
                        "backgroundSize": "cover",
                        "backgroundPosition": "center",
                        "backgroundRepeat": "no-repeat",
                        "minHeight": "500px",
                        "padding": "20px"
                    }
                )
            ],
            className="shadow"
        )
    ],
    fluid=True,
    className="mt-4"
)
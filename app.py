from dash import Dash, html, dcc, page_container
import dash_bootstrap_components as dbc

# Initialisation de l'application multipages

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.Div(
                "Application des M1 MECEN",
                className="navbar-brand mb-0 h1 text-white fw-bold"
            ),
            dbc.Nav(
                [
                    dbc.NavLink("Comparaison entre région", href="/", className="text-white"),
                    dbc.NavLink("Affichage des données", href="/page2", className="text-white"),
                    dbc.NavLink("Aide en ligne", href="/page3", className="text-white"),
                ],
                pills=False,
                className="ms-auto"
            )
        ],
        fluid=True
    ),
    color="primary",
    dark=True,
    className="mb-4"
)

app.layout = dbc.Container(
    [
        navbar,
        page_container
    ],
    fluid=True
)

if __name__ == "__main__":
    app.run(debug=True)
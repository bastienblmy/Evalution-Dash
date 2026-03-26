from dash import Dash
import dash_bootstrap_components as dbc
from pages.page2 import layout

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout

if __name__ == "__main__":
    app.run(debug=True)
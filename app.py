import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Import pages (removed location for now)
from pages import home, trends, seasonal, conditions, insights, about

# Import callbacks
from callbacks import callbacks

# Initialize the app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True   # ✅ IMPORTANT FIX
)
server = app.server

# Sidebar
sidebar = html.Div(
    [
        html.H2("Weather Dashboard", className="display-5"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Temperature Trends", href="/trends", active="exact"),
                dbc.NavLink("Seasonal Analysis", href="/seasonal", active="exact"),
                dbc.NavLink("Weather Conditions", href="/conditions", active="exact"),
                dbc.NavLink("Insights", href="/insights", active="exact"),
                dbc.NavLink("About", href="/about", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa"
    },
)

# Content
content = html.Div(
    id="page-content",
    style={"margin-left": "18rem", "padding": "2rem 1rem"}
)

# Layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Routing
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/trends":
        return trends.layout
    elif pathname == "/seasonal":
        return seasonal.layout
    elif pathname == "/conditions":
        return conditions.layout
    elif pathname == "/insights":
        return insights.layout
    elif pathname == "/about":
        return about.layout
    else:
        return html.H1("404: Page not found")

# Register callbacks
callbacks.register_callbacks(app)

# Run
if __name__ == "__main__":
    app.run(debug=True)
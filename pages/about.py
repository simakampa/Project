from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        html.H1("About This Dashboard"),
        html.P("This weather dashboard visualizes data collected from NOAA weather stations."),

        html.H3("Dataset Details"),
        html.Ul([
            html.Li("Source: NOAA Weather Data"),
            html.Li("Columns used: TEMP (Average Temperature), PRCP (Precipitation), WDSP (Wind Speed), VISIB (Visibility), MAX, MIN, DATE, LATITUDE, LONGITUDE"),
        ]),

        html.H3("Tools & Technologies"),
        html.Ul([
            html.Li("Dash: Python framework for building interactive web applications"),
            html.Li("Plotly: For charts and data visualization"),
            html.Li("Bootstrap: For responsive styling"),
            html.Li("Pandas: For data processing and aggregation"),
        ]),

        html.H3("Purpose"),
        html.P("The dashboard provides insights into weather patterns, temperature trends, seasonal variations, rainfall, wind speed, and visibility.")
    ])
])
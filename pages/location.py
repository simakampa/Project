from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from utils.data_loader import load_weather_data
from pages import home, trends, seasonal, conditions, insights, about
# Load data
df = load_weather_data()

# Optional: if you have a 'NAME' column for station
if 'NAME' not in df.columns:
    df['NAME'] = 'Weather Station'

# Map figure
def get_station_map():
    fig = px.scatter_mapbox(
        df.drop_duplicates(subset=['LATITUDE','LONGITUDE']),
        lat='LATITUDE',
        lon='LONGITUDE',
        hover_name='NAME',
        zoom=5,
        height=500,
        title="Weather Station Location"
    )
    fig.update_layout(
        mapbox_style="open-street-map",
        margin=dict(l=20,r=20,t=40,b=20)
    )
    return fig

# Layout
layout = html.Div([
    dbc.Container([
        html.H1("Weather Station Location"),
        html.P("Visualize where the weather data is collected from."),

        dcc.Graph(id='station-map', figure=get_station_map())
    ])
])
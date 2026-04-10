from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from utils.data_loader import load_weather_data

# Load data
df = load_weather_data()

# Ensure year is integer (SAFE FIX)
df['year'] = df['year'].astype(int)

# Rainfall
def get_rainfall_chart(year_range=None):
    if year_range:
        start, end = year_range
        df_filtered = df[(df['year'] >= start) & (df['year'] <= end)]
    else:
        df_filtered = df

    fig = px.line(
        df_filtered, x='DATE', y='PRCP',
        title='Daily Rainfall Over Time',
        labels={'DATE': 'Date', 'PRCP': 'Rainfall (mm)'}
    )
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig

# Wind
def get_wind_chart(year_range=None):
    if year_range:
        start, end = year_range
        df_filtered = df[(df['year'] >= start) & (df['year'] <= end)]
    else:
        df_filtered = df

    fig = px.line(
        df_filtered, x='DATE', y='WDSP',
        title='Daily Wind Speed Over Time',
        labels={'DATE': 'Date', 'WDSP': 'Wind Speed (km/h)'}
    )
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig

# Visibility
def get_visibility_chart(year_range=None):
    if year_range:
        start, end = year_range
        df_filtered = df[(df['year'] >= start) & (df['year'] <= end)]
    else:
        df_filtered = df

    fig = px.line(
        df_filtered, x='DATE', y='VISIB',
        title='Daily Visibility Over Time',
        labels={'DATE': 'Date', 'VISIB': 'Visibility (km)'}
    )
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig

# Layout
layout = html.Div([
    dbc.Container([
        html.H1("Weather Conditions"),
        html.P("Analyze rainfall, wind speed, and visibility over time."),

        html.Label("Select Year Range:"),
        dcc.RangeSlider(
            id='conditions-year-range',
            min=int(df['year'].min()),
            max=int(df['year'].max()),
            step=1,
            marks={int(y): str(y) for y in sorted(df['year'].unique())},  # ✅ FIXED
            value=[int(df['year'].min()), int(df['year'].max())]
        ),

        dbc.Row([
            dbc.Col(dcc.Graph(id='rainfall-chart', figure=get_rainfall_chart()), width=12),
            dbc.Col(dcc.Graph(id='wind-chart', figure=get_wind_chart()), width=12),
            dbc.Col(dcc.Graph(id='visibility-chart', figure=get_visibility_chart()), width=12),
        ])
    ])
])
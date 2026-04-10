from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from utils.data_loader import load_weather_data

# Load data
df = load_weather_data()

# Ensure year is integer (SAFE FIX)
df['year'] = df['year'].astype(int)

# Generate line chart (DATE vs TEMP, MAX, MIN)
def get_trends_chart(year_range=None):
    if year_range:
        start, end = year_range
        df_filtered = df[(df['year'] >= start) & (df['year'] <= end)]
    else:
        df_filtered = df

    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df_filtered['DATE'], y=df_filtered['TEMP'],
        mode='lines',
        name='Average Temp',
        line=dict(color='orange', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=df_filtered['DATE'], y=df_filtered['MAX'],
        mode='lines',
        name='Max Temp',
        line=dict(color='red', width=2, dash='dash')
    ))

    fig.add_trace(go.Scatter(
        x=df_filtered['DATE'], y=df_filtered['MIN'],
        mode='lines',
        name='Min Temp',
        line=dict(color='blue', width=2, dash='dash')
    ))

    fig.update_layout(
        title='Temperature Trends Over Time',
        xaxis_title='Date',
        yaxis_title='Temperature (°C)',
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(x=0, y=1.1, orientation='h')
    )

    return fig

# Layout
layout = html.Div([
    dbc.Container([
        html.H1("Temperature Trends"),
        html.P("Analyze average, maximum, and minimum temperatures over time."),

        html.Label("Select Year Range:"),
        dcc.RangeSlider(
            id='trends-year-range',
            min=int(df['year'].min()),
            max=int(df['year'].max()),
            step=1,
            marks={int(y): str(y) for y in sorted(df['year'].unique())},  # ✅ FIXED
            value=[int(df['year'].min()), int(df['year'].max())]
        ),

        dcc.Graph(id='trends-temp-chart', figure=get_trends_chart())
    ])
])
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from utils.data_loader import load_weather_data
import pandas as pd

# Load data
df = load_weather_data()

# Ensure DATE is datetime (SAFE FIX)
df['DATE'] = pd.to_datetime(df['DATE'])

# Create month names
df['month_name'] = df['DATE'].dt.strftime('%b')

# Correct month order
month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']


# -------- Temperature Chart -------- #
def get_seasonal_temp_chart():
    monthly_avg = df.groupby('month_name')['TEMP'].mean().reindex(month_order)

    fig = px.bar(
        x=monthly_avg.index,
        y=monthly_avg.values,
        labels={'x':'Month', 'y':'Average Temperature (°C)'},
        title='Average Monthly Temperature'
    )

    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig


# -------- Rainfall Chart -------- #
def get_seasonal_prcp_chart():
    monthly_prcp = df.groupby('month_name')['PRCP'].mean().reindex(month_order)

    fig = px.bar(
        x=monthly_prcp.index,
        y=monthly_prcp.values,
        labels={'x':'Month', 'y':'Average Rainfall (mm)'},
        title='Average Monthly Rainfall'
    )

    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig


# -------- Layout -------- #
layout = html.Div([
    dbc.Container([
        html.H1("Seasonal Analysis"),
        html.P("Explore monthly patterns in temperature and rainfall."),

        dbc.Row([
            dbc.Col(
                dcc.Graph(id='seasonal-temp-chart', figure=get_seasonal_temp_chart()),
                width=6
            ),
            dbc.Col(
                dcc.Graph(id='seasonal-prcp-chart', figure=get_seasonal_prcp_chart()),
                width=6
            )
        ])
    ])
])
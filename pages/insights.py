from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from utils.data_loader import load_weather_data
import pandas as pd

# Load data
df = load_weather_data()

# Ensure DATE is datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Month names
df['month_name'] = df['DATE'].dt.strftime('%b')

# Correct month order
month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']


# -------- Monthly Avg Temp -------- #
monthly_avg_temp = df.groupby('month_name')['TEMP'].mean().reindex(month_order)

fig_temp_month = px.bar(
    x=monthly_avg_temp.index,
    y=monthly_avg_temp.values,
    labels={'x':'Month','y':'Avg Temp (°C)'},
    title='Average Temperature by Month'
)


# -------- Monthly Rainfall -------- #
monthly_avg_prcp = df.groupby('month_name')['PRCP'].mean().reindex(month_order)

fig_prcp_month = px.bar(
    x=monthly_avg_prcp.index,
    y=monthly_avg_prcp.values,
    labels={'x':'Month','y':'Avg Rainfall (mm)'},
    title='Average Rainfall by Month'
)


# -------- Temp Comparison -------- #
max_temp = df['MAX'].max()
avg_temp = df['TEMP'].mean()

fig_temp_diff = px.pie(
    names=['Average Temp', 'Maximum Temp'],
    values=[avg_temp, max_temp],
    title='Average vs Maximum Temperature'
)


# -------- Layout -------- #
layout = html.Div([
    dbc.Container([
        html.H1("Insights & Key Findings"),
        html.P("Summarizing the main trends and patterns in the weather data."),

        html.Ul([
            html.Li("Temperature shows seasonal variation, peaking in hotter months."),
            html.Li("Rainfall varies across the year with noticeable peaks."),
            html.Li("Maximum temperature is higher than the average daily temperature."),
            html.Li("Wind speed and visibility fluctuate moderately.")
        ]),

        dbc.Row([
            dbc.Col(dcc.Graph(id='insight-temp-month', figure=fig_temp_month), width=4),
            dbc.Col(dcc.Graph(id='insight-prcp-month', figure=fig_prcp_month), width=4),
            dbc.Col(dcc.Graph(id='insight-temp-diff', figure=fig_temp_diff), width=4),
        ])
    ])
])
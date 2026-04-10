from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from utils.data_loader import load_weather_data

# Load the data
df = load_weather_data()

# ----------- LINE CHART FUNCTION ----------- #
def get_line_chart(year=None):
    if year:
        df_year = df[df['year'] == year]
    else:
        df_year = df

    fig = px.line(
        df_year,
        x='DATE',
        y='TEMP',
        title='Daily Average Temperature',
        labels={'DATE': 'Date', 'TEMP': 'Temperature (°C)'}
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        hovermode="x unified"   # ✅ slight improvement
    )

    return fig


# ----------- SUMMARY STATS FUNCTION ----------- #
def get_summary_stats(year=None):
    if year:
        df_year = df[df['year'] == year]
    else:
        df_year = df

    stats = {
        'Avg Temp': round(df_year['TEMP'].mean(), 2),
        'Max Temp': df_year['MAX'].max(),
        'Min Temp': df_year['MIN'].min()
    }

    return stats


# ----------- LAYOUT ----------- #
layout = html.Div([
    dbc.Container([

        html.H1("Weather Dashboard Overview"),
        html.P("Quick summary of weather conditions and temperature trends."),

        # -------- Year Filter -------- #
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='home-year-dropdown',
            options=[{'label': int(y), 'value': int(y)} for y in sorted(df['year'].unique())],  # ✅ fixed
            value=None,
            placeholder="All Years",
            clearable=True   # ✅ small improvement
        ),

        # -------- Line Chart -------- #
        dcc.Graph(
            id='home-temp-line-chart',
            figure=get_line_chart()
        ),

        # -------- Summary Cards -------- #
        dbc.Row([

            dbc.Col(
                dbc.Card([
                    dbc.CardHeader("Average Temperature"),
                    dbc.CardBody(
                        html.H4(
                            f"{get_summary_stats()['Avg Temp']} °C",  # ✅ formatted
                            className="card-title"
                        )
                    )
                ], color="info", inverse=True),
                width=4
            ),

            dbc.Col(
                dbc.Card([
                    dbc.CardHeader("Maximum Temperature"),
                    dbc.CardBody(
                        html.H4(
                            f"{get_summary_stats()['Max Temp']} °C",
                            className="card-title"
                        )
                    )
                ], color="danger", inverse=True),
                width=4
            ),

            dbc.Col(
                dbc.Card([
                    dbc.CardHeader("Minimum Temperature"),
                    dbc.CardBody(
                        html.H4(
                            f"{get_summary_stats()['Min Temp']} °C",
                            className="card-title"
                        )
                    )
                ], color="primary", inverse=True),
                width=4
            ),

        ], className="mt-4")  # ✅ spacing improvement

    ])
])
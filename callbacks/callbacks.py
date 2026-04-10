from dash import Input, Output
from pages import home, trends, conditions

def register_callbacks(app):

    # HOME
    @app.callback(
        Output('home-temp-line-chart', 'figure'),
        Input('home-year-dropdown', 'value')
    )
    def update_home_chart(year):
        fig = home.get_line_chart(year)
        return fig   # ✅ FIXED (removed extra fig)

    # TRENDS
    @app.callback(
        Output('trends-temp-chart', 'figure'),
        Input('trends-year-range', 'value')
    )
    def update_trends_chart(year_range):
        return trends.get_trends_chart(year_range)

    # CONDITIONS
    @app.callback(
        Output('rainfall-chart', 'figure'),
        Output('wind-chart', 'figure'),
        Output('visibility-chart', 'figure'),
        Input('conditions-year-range', 'value')
    )
    def update_conditions_charts(year_range):
        return (
            conditions.get_rainfall_chart(year_range),
            conditions.get_wind_chart(year_range),
            conditions.get_visibility_chart(year_range)
        )
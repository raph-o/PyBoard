from dash import Output, Input, callback
from core.main import df
import plotly.express as px


@callback(
    Output("graph", "figure"),
    Input("country", "value"))
def generate_chart_callback(selected_countries):
    return generate_chart(selected_countries)


def generate_chart(selected_countries):
    if selected_countries is None:
        return px.bar(title="Please select a country")

    filtered_df = df[df['country'].isin(selected_countries)]
    fig = px.bar(filtered_df, x='date', y='value', color='country', title=f'GES for {selected_countries}',
                 barmode='group', range_x=[1990, 2020])
    return fig

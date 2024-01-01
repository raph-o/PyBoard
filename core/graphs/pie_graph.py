from dash import Output, Input, callback
from core.main import df
import plotly.express as px


@callback(
    Output("pie", "figure"),
    Input("country", "value"))
def generate_pie_callback(selected_countries):
    return generate_chart(selected_countries)


def generate_chart(selected_countries):
    if selected_countries is None:
        return px.bar(title="Please select a country")

    filtered_df = df[df['country'].isin(selected_countries)]
    fig = px.pie(filtered_df, values='value', names='country', title=f'GES for {selected_countries}')
    return fig

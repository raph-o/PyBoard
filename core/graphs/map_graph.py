from dash import Output, Input, callback
from core.main import df

import plotly.express as px
import plotly.graph_objects as go


@callback(
    Output("geo", "figure"),
    Input("country", "value"))
def generate_map_callback(selected_countries):
    return generate_map(selected_countries)


def generate_map(selected_countries):
    if selected_countries is None:
        return px.choropleth(title="Please select a country")

    fig = go.Figure()
    filtered_df = df[df['country'].isin(selected_countries)]
    for country in selected_countries:
        country_data = filtered_df[filtered_df['country'] == country]
        fig.add_trace(
            go.Choropleth(
                locations=country_data['country_code'],
                z=country_data['value'],
                text=country_data['country'],
                hoverinfo="location+z+text",
                colorscale="Viridis",
                showscale=False,
                locationmode='ISO-3'
            )
        )

    fig.update_layout(
        title="Choropleth Map",
        geo=dict(
            showframe=False,
            projection_type='natural earth'
        )
    )
    return fig
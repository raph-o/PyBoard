from dash import Output, Input, callback

import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs import Figure


@callback(
    Output("geo", "figure"),
    Input("country", "value"))
def generate_map_callback(selected_countries) -> Figure:
    """
    Enregistre le callback pour gérer la map. Notons l'utilisation d'import dans la fonction afin d'éviter une circular dépendency error

    :param selected_countries: pays sélectionnés dans le formulaire
    :return: La map mise à jour
    """
    from main import df
    return generate_map_graph(selected_countries, df)


def generate_map_graph(selected_countries, df) -> Figure:
    """
    Créer la figure map

    :param selected_countries: pays sélectionnés dans le formulaire
    :param df: données de traitement pour la liste des pays sélectionnés
    :return: Une figure map
    """
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
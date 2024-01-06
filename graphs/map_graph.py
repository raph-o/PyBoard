from dash import Output, Input, callback

import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs import Figure


@callback(
    Output("geo", "figure"),
    Input("country", "value"),
    Input("date_dropdown", "value"))
def generate_map_callback(selected_countries, selected_date) -> Figure:
    """
    Enregistre le callback pour gérer la map. Notons l'utilisation d'import dans la fonction afin d'éviter une circular dépendency error

    :param selected_date: date sélectionnée dans le formulaire
    :param selected_countries: pays sélectionnés dans le formulaire
    :return: La map mise à jour
    """
    from main import df
    return generate_map_graph(selected_countries, selected_date, df)


def generate_map_graph(selected_countries, selected_date, df) -> Figure:
    """
    Créer la figure map

    :param selected_countries: pays sélectionnés dans le formulaire
    :param selected_date: date sélectionnée dans le formulaire
    :param df: données de traitement pour la liste des pays sélectionnés
    :return: Une figure map
    """
    if selected_countries is None:
        return px.choropleth(title="Veuillez sélectionner un pays")

    fig = go.Figure()
    filtered_df = df[df['country'].isin(selected_countries) & (df['date'] == selected_date)]
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
    return fig.update_layout(
        geo=dict(
            showframe=False,
            projection_type='equirectangular'
        ),
    )

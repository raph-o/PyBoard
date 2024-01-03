from dash import Output, Input, callback

import plotly.express as px
from plotly.graph_objs import Figure


@callback(
    Output("line", "figure"),
    Input("country", "value"))
def generate_line_callback(selected_countries) -> Figure:
    """
    Enregistre le callback pour gérer les lignes. Notons l'utilisation d'import dans la fonction afin d'éviter une circular dépendency error

    :param selected_countries: liste des pays sélectionnés dans le formulaire
    :return: Les lignes mise à jour
    """
    from main import df
    return generate_line_graph(selected_countries, df)


def generate_line_graph(selected_countries, df) -> Figure:
    """
    Créer la figure lignes

    :param selected_countries: pays sélectionnés dans le formulaire
    :param df: données de traitement pour la liste des pays sélectionnés
    :return: Une figure lignes
    """
    if selected_countries is None:
        return px.bar(title="Please select a country")

    filtered_df = df[df['country'].isin(selected_countries)]
    fig = px.line(filtered_df, x='date', y='value', color='country', title=f'GES for {selected_countries}', range_x=[1990, 2020])
    return fig

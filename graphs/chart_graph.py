from dash import Output, Input, callback
import plotly.express as px
from plotly.graph_objs import Figure


@callback(
    Output("graph", "figure"),
    Input("country", "value"))
def generate_chart_callback(selected_countries) -> Figure:
    """
    Enregistre le callback pour gérer la charte. Notons l'utilisation d'import dans la fonction afin d'éviter une circular dépendency error

    :param selected_countries: liste des pays sélectionnés dans le formulaire
    :return: La charte mise à jour
    """
    from main import df
    return generate_chart(selected_countries, df)


def generate_chart(selected_countries, df) -> Figure:
    """
    Créer la charte
    :param selected_countries: liste des pays sélectionnés dans le formulaire
    :param df: données de traitement pour la liste des pays sélectionnés
    :return: Une figure charte
    """
    if selected_countries is None:
        return px.bar(title="Please select a country")

    filtered_df = df[df['country'].isin(selected_countries)]
    fig = px.bar(filtered_df, x='date', y='value', color='country', title=f'GES for {selected_countries}',
                 barmode='group', range_x=[1990, 2020])
    return fig

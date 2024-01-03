from dash import Output, Input, callback
import plotly.express as px
from plotly.graph_objs import Figure


@callback(
    Output("pie", "figure"),
    Input("country", "value"))
def generate_pie_callback(selected_countries) -> Figure:
    """
    Enregistre le callback pour gérer le diagramme circulaire. Notons l'utilisation d'import dans la fonction afin d'éviter une circular dépendency error

    :param selected_countries: pays sélectionnés dans le formulaire
    :return: La map mise à jour
    """
    from main import df
    return generate_pie_graph(selected_countries, df)


def generate_pie_graph(selected_countries, df) -> Figure:
    """
    Créer la figure diagramme circulaire

    :param selected_countries: pays sélectionnés dans le formulaire
    :param df: données de traitement pour la liste des pays sélectionnés
    :return: Une figure diagramme circulaire
    """
    if selected_countries is None:
        return px.bar(title="Please select a country")

    filtered_df = df[df['country'].isin(selected_countries)]
    fig = px.pie(filtered_df, values='value', names='country', title=f'GES for {selected_countries}')
    return fig

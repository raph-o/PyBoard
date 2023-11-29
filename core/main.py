from dash import Dash, dcc, html, Input, Output, callback
from api import api

import plotly.express as px
import json
import pandas as pd


results = api.get_data()
json_results = []
for result in results:
    json_results.append(result.to_json())
parsed_results = [json.loads(result) for result in json_results]
df = pd.read_json(json.dumps(parsed_results))
available_countries = df['countryiso3code'].unique()

app = Dash(__name__)
app.layout = html.Div([
    html.H4('GES per country'),
    dcc.Graph(id="graph"),
    html.P("Country:"),
    dcc.Dropdown(id='country',
                 options=[{'label': country, 'value': country} for country in available_countries],
                 value=[],
                 multi=True
                 ),
    ])


@app.callback(
    Output("graph", "figure"),
    Input("country", "value"))
def generate_chart(selected_countries):
    if selected_countries is None:
        return px.bar(title="Please select a country")

    filtered_df = df[df['countryiso3code'].isin(selected_countries)]
    fig = px.bar(filtered_df, x='date', y='value', color='countryiso3code', title=f'GES for {selected_countries}', barmode='group')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

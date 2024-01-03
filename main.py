from dash import Dash
from io import StringIO
from api.Api import Api
from layout import get_layout

"""
Ces importations sont nécessaires afin de pouvoir afficher et mettre à jour les différents graphiques sur le dashboard
"""
from graphs.map_graph import generate_map_callback
from graphs.pie_graph import generate_pie_callback
from graphs.chart_graph import generate_chart_callback
from graphs.line_graph import generate_line_callback

import pandas as pd

api = Api()

json_string = api.get_result()
json_stream = StringIO(json_string)
df = pd.read_json(json_stream)
available_countries = df['country'].unique()

app = Dash(__name__)
app.layout = get_layout(available_countries)

if __name__ == '__main__':
    app.run_server(debug=True)

from dash import Dash
from io import StringIO
from api.Api import Api
from core.layout import get_layout
from core.graphs.line_graph import generate_line_callback
from core.graphs.pie_graph import generate_pie_callback
from core.graphs.chart_graph import generate_chart_callback
from core.graphs.map_graph import generate_map_callback

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

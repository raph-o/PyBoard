from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import json
import os
import pandas as pd

from api import api

results = api.get_data()
json_results = []

for result in results:
    json_results.append(result.to_json())

parsed_results = [json.loads(result) for result in json_results]

df = pd.read_json(json.dumps(parsed_results))
print(df)

# créer un histogram GES/year
fig = px.bar(df, x='date', y='value', color='countryiso3code')

fig.show()

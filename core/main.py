from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import json
import os
import pandas as pd

json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temp', 'GesPerRegion.json')

df = pd.read_json(json_path)
df = df.dropna(subset=["value"])

# créer un histogram GES/year
fig = px.bar(df, x="date", y="value", color="countryiso3code")

fig.show()

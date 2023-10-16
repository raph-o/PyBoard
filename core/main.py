from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import json
import os
import pandas as pd
from api.Api import Api

x = Api()

df = pd.read_json(x.get_result())
print(df)



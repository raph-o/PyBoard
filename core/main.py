from io import StringIO

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import json
import os
import pandas as pd
from api import *
from api.Api import Api

x = Api()

json_string = x.get_result()
json_stream = StringIO(json_string)
df = pd.read_json(json_stream)

print(Api().get_result())




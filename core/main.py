from dash import Dash
from io import StringIO
from api.Api import Api
from core.layout import get_layout

import pandas as pd
import graphs


api = Api()

json_string = api.get_result()
json_stream = StringIO(json_string)
df = pd.read_json(json_stream)
available_countries = df['country'].unique()
print(df)

app = Dash(__name__)
app.layout = get_layout(available_countries)


if __name__ == '__main__':
    app.run_server(debug=True)

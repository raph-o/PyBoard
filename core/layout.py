from dash import html, dcc


def get_layout(available_countries):
    return html.Div([
        html.H4('GES per country'),
        html.P("Country:"),
        dcc.Dropdown(id='country',
                     options=[{'label': country, 'value': country} for country in available_countries],
                     value=[],
                     multi=True
                     ),
        dcc.Graph(id="graph"),
        dcc.Graph(id="geo"),
        dcc.Graph(id="pie"),
        dcc.Graph(id="line"),
    ])

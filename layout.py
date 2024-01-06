from dash import html, dcc


def get_layout(available_countries, available_dates):
    default_selected_countries = ['France', 'Allemagne']

    return html.Div([
        html.H1('GES per country', style={'color': '#333', 'marginBottom': 20, 'font-family': 'Arial, sans-serif',
                                          'text-align': 'center'}),
        html.P("Country:", style={'fontSize': 18, 'font-family': 'Georgia, serif'}),
        dcc.Dropdown(
            id='country',
            options=[{'label': country, 'value': country} for country in available_countries],
            value=default_selected_countries,
            multi=True,
            style={'marginBottom': 20}
        ),
        dcc.Graph(id="graph", style={'backgroundColor': '#f9f9f9', 'marginBottom': 20}),

        dcc.Dropdown(id='date_dropdown',
                     options=[{'label': date, 'value': date} for date in available_dates], value=1990),
        html.Div([
            dcc.Graph(id="geo", style={'backgroundColor': '#ffffff', 'width': '40%', 'flex': 1}),
            dcc.Graph(id="pie", style={'backgroundColor': '#f9f9f9', 'width': '40%', 'flex': 1}),
        ], style={'marginBottom': 20, 'display': 'flex', 'justify-content': 'space-between'}),

        dcc.Graph(id="line", style={'backgroundColor': '#ffffff', 'marginBottom': 20}),
    ], style={'backgroundColor': '#f4f4f4', 'padding': '20px'})

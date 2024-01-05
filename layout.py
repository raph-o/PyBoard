from dash import html, dcc


def get_layout(available_countries):
    default_selected_countries = ['France', 'Allemagne']  # Ajout des pays par défaut

    return html.Div([
        html.H1('GES per country', style={'color': '#333', 'marginBottom': 20, 'font-family': 'Arial, sans-serif',
                                          'text-align': 'center'}),
        html.P("Country:", style={'fontSize': 18, 'font-family': 'Georgia, serif'}),
        dcc.Dropdown(
            id='country',
            options=[{'label': country, 'value': country} for country in available_countries],
            value=default_selected_countries,  # Définir les pays par défaut
            multi=True,
            style={'marginBottom': 20}
        ),
        dcc.Graph(id="graph", style={'backgroundColor': '#f9f9f9', 'marginBottom': 20}),

        html.Div([
            dcc.Graph(id="geo", style={'backgroundColor': '#ffffff', 'width': '40%', 'flex': 1}),
            dcc.Graph(id="pie", style={'backgroundColor': '#f9f9f9', 'width': '40%', 'flex': 1}),
        ], style={'marginBottom': 20, 'display': 'flex', 'justify-content': 'space-between'}),

        dcc.Graph(id="line", style={'backgroundColor': '#ffffff', 'marginBottom': 20}),
    ], style={'backgroundColor': '#f4f4f4', 'padding': '20px'})

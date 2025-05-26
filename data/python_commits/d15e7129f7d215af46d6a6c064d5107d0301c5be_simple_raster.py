    dcc.Store(id='data-store'),  # Store for holding uploaded data
    dbc.Row([
        dbc.Col(dcc.Upload(
            id='upload-spike-times',
            children=html.Div(['Spike times', html.A('')]),
            style={'width': '100%', 'height': '60px', 'lineHeight': '60px',
                   'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                   'textAlign': 'center', 'margin': '10px'},
            multiple=False
        ), width=4),
        dbc.Col(dcc.Upload(
            id='upload-spike-clusters',
            children=html.Div(['Spike clusters', html.A('')]),
            style={'width': '100%', 'height': '60px', 'lineHeight': '60px',
                   'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                   'textAlign': 'center', 'margin': '10px'},
            multiple=False
        ), width=4),
        dbc.Col(dcc.Upload(
            id='upload-behavior',
            children=html.Div(['Behavior', html.A('')]),
            style={'width': '100%', 'height': '60px', 'lineHeight': '60px',
                   'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                   'textAlign': 'center', 'margin': '10px'},
            multiple=False
        ), width=4)
    ]),
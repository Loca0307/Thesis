    dbc.Container(
        dbc.Row(
            [dbc.Col(
                dcc.Upload(
                    id='upload-spike-times',
                    children=html.Div(['Drop SPIKETIMES or ', html.A('Select Files')]),
                    style={
                        'width': '20%', 'height': '40px', 'lineHeight': '40px',
                        'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                        'textAlign': 'center', 'margin': '10px'
                    },
                    multiple=False
                )
            ),
            dbc.Col(
                dcc.Upload(
                    id='upload-spike-clusters',
                    children=html.Div(['Drop SPIKECLUSTERS or ', html.A('Select Files')]),
                    style={
                        'width': '20%', 'height': '40px', 'lineHeight': '40px',
                        'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                        'textAlign': 'center', 'margin': '10px'
                    },
                    multiple=False
                )
            ),
            dbc.Col(
                dcc.Upload(
                    id='upload-behavior',
                    children=html.Div(['Drop BEHAVIOR or ', html.A('Select Files')]),
                    style={
                        'width': '20%', 'height': '40px', 'lineHeight': '40px',
                        'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                        'textAlign': 'center', 'margin': '10px'
                    },
                    multiple=False
                )
            )]
        )
    ),
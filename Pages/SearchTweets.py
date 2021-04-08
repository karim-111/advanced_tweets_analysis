import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc



tab1_content = html.Div(
    html.Div(
        [
            html.Div(
                className="inputAndSubmit",
                children=[

                    dbc.Input(id='my-input', value='', type='text'),
                    html.Button(id='submit-button-state', n_clicks=0, children="Search",
                                className="hhhhhhhhhhh"),
                ]),
            html.Div(id='table'),
            html.Div(id='table2'),

        ]
    ),
    className="mt-3",
)
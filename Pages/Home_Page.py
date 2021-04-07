import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from Components.Table import generate_table
from API.Scraping_Tweets import search
from dash.exceptions import PreventUpdate
import pandas as pd

from App import app

layout = html.Div(
    className="first",

    children=[
        html.Div(
            className="LogoAndTitle",
            children=[
                html.Img(className="hh", src=("/assets/Logo.png")),
                html.H1(children=" TweeMusk", className='titre'),
            ]
        ),
        html.Div(
            className="second",

            children=[
                html.Div(
                    className='trrrrr',
                    children=[

                        html.Div(
                            className="formulaire",
                            children=[
                                html.P(
                                    className='theParagraph',
                                    children=["Enter your request"]
                                ),
                                html.Div(
                                    className="inputAndSubmit",
                                    children=[

                                        dbc.Input(id='my-input', value='', type='text'),
                                        html.Button(id='submit-button-state', n_clicks=0, children="Search",
                                                    className="hhhhhhhhhhh"),
                                    ]),

                            ]
                        ),

                    ]
                ),

                html.Br(),
                html.Div(id='intermediate-value', style={'display': 'none'}),
                html.Div(id='table'),
                html.Div(id="hk")

            ])

    ])


@app.callback(
    Output(component_id='output-data-upload', component_property='children'),
    Input('submit-button-state', 'n_clicks'),
    State('my-input', 'value')
)
def update_output_div(n_clicks, input_value):
    if n_clicks is None:
        raise PreventUpdate
    else:
        if input_value != "":
            df = search(input_value)
            return df.to_json(date_format='iso', orient='split')


@app.callback(Output('table', 'children'), Input('output-data-upload', 'children'))
def update_table(jsonified_cleaned_data):
    if jsonified_cleaned_data:
        dff = pd.read_json(jsonified_cleaned_data, orient='split')
        table = generate_table(dff)
        return table



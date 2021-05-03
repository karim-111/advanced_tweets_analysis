import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
import pandas as pd
import datetime
import io
import dash_table
from Components.Table2 import generate_table2

tab1_content = html.Div(
    className='EnglobanteSearch',
    children=[
        html.Div(
            className="EnglobanteDesInput",
            children=[
                html.Div(
                    className="inputAndSubmit",
                    children=[
                        html.Div(
                            className="ne",
                            children=[
                                html.Div(

                                    className="second_input",
                                    children=[
                                        html.H4(className='titleofinput', children=("Hashtag or word")),
                                        dbc.Input(id='my-input', value='', type='text', placeholder='#hashtag'),
                                    ]
                                ),
                                html.Div(
                                    className="select_input",
                                    children=[
                                        html.H4(className='titleofinput', children=("Number of tweets")),

                                        dcc.Dropdown(
                                            className="select_input",
                                            id='demo-dropdown',
                                            options=[
                                                {'label': '40', 'value': 40},
                                                {'label': '100', 'value': 100},
                                                {'label': '200', 'value': 200},
                                                {'label': '500', 'value': 500},
                                                {'label': '1000', 'value': 1000},
                                                {'label': '2000', 'value': 2000},
                                                {'label': '5000', 'value': 5000},
                                                {'label': '10000', 'value': 10000},

                                            ],

                                            value=40),

                                    ]),

                            ]
                        ),

                        html.Div(
                            className="first_input",
                            children=[
                                html.H4(className='titleofinput', children=("Name of the twitter account")),
                                dbc.Input(id='my-input-by-name', value='', type='text', placeholder="Name"), ]
                        ),

                        html.Button(id='submit-button-state', n_clicks=0, children="Search",
                                    className="hhhhhhhhhhh"),
                        dcc.Loading(
                            style={"marginTop": '30px', "marginBottom": "2Opx"},
                            id="loading-1",
                            type="default",
                            children=html.Div(id="loading-output-1")
                        ),
                        html.H1(""),
                        html.H1(""),
                        html.H1(""),
                        html.H4(className='titleofinput', children="Or"),

                        dcc.Upload(
                            id='upload-data',
                            children=html.Div([
                                'Drag and Drop or ',
                                html.A('Select Files')
                            ]),
                            style={
                                'width': '100%',
                                'height': '60px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '10px'
                            },
                            # Allow multiple files to be uploaded
                            multiple=True
                        ),

                    ]),
            ],

        ),

    ],
)


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            df.to_csv("wat.csv")
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return [html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),
        generate_table2(df),
        html.Hr(),  # horizontal line

    ]), df]

# html.Div(id='table'),
#    html.Div(id='table2'),

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
from Components.Table import generate_table
from API.wat import search
from dash.exceptions import PreventUpdate
import pandas as pd
from Components.NavBar import navbar

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    style={

    },

    children=[
        navbar,
        html.Div(
            style={
                'marginTop': '100px',
                'display': 'flex',
                'alignItems': "center",
                'justifyContent': 'center',
                'flexDirection': 'column',

            }, children=[
                html.H6(children="Entrez le mot à rechercher : ", style={"fontSize": 19}),
                html.Div(["Input: ",
                          dbc.Input(id='my-input', value='', type='text')]),
                dbc.Button(id='submit-button-state', n_clicks=0, children='Submit', color="primary", className="mr-1"),

                html.Br(),
                html.Div(id='intermediate-value', style={'display': 'none'}),
                html.Div(id='table'),
            ])

    ])


@app.callback(
    Output(component_id='intermediate-value', component_property='children'),
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


@app.callback(Output('table', 'children'), Input('intermediate-value', 'children'))
def update_table(jsonified_cleaned_data):
    if jsonified_cleaned_data:
        dff = pd.read_json(jsonified_cleaned_data, orient='split')
        table = generate_table(dff)
        return table


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)

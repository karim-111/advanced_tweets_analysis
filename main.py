import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from layouts import layout1
from Pages import Home_Page
from Components.Table import generate_table
from API.Scraping_Tweets import search
from dash.exceptions import PreventUpdate
import pandas as pd
from API.Cleaning_Tweets import clean
import time
import plotly.express as px

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
len_data = 3500

app.layout = html.Div([
    dcc.Store(id='session',
              data=[]),
    dcc.Store(id="clean_df",
              data=[]),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

page_1 = layout1


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/login':
        return page_1

    if pathname == '/Home':
        return Home_Page.layout


# Callback Pour la recherche des tweets
# Et enregistrement dans le dcc.store
@app.callback(
    Output('session', 'data'),
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


# Affectation du dataframe collecter par tweepy a la table
@app.callback(Output('table', 'children'), Input('session', 'data'))
def update_table(jsonified_cleaned_data):
    if jsonified_cleaned_data:
        dff = pd.read_json(jsonified_cleaned_data, orient='split')
        table = generate_table(dff)
        return table


# Cleaning the tweets and store it

@app.callback(Output('jecpas', 'children'), Output('clean_df', 'data'), Input('session', 'data'))
def update_table_clean(jsonified_cleaned_data):
    if jsonified_cleaned_data:
        df = pd.read_json(jsonified_cleaned_data, orient='split')
        df['Text'] = df['Text'].apply(clean)
        table = generate_table(df)
        return table, df.to_json(date_format='iso', orient='split')
    else:
        return [], []



if __name__ == '__main__':
    app.run_server(debug=True, port=8052)

import os
import glob
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import flask
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from API.Utils import generate_word_cloud
from layouts import layout1
from Pages import Home_Page
from Components.Table import generate_table
from API.Scraping_Tweets import search
from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime
from API.Cleaning_Tweets import clean
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


@app.callback(Output('table', 'children'), Input('session', 'data'))
def update_table(jsonified_cleaned_data):
    if jsonified_cleaned_data:
        dff = pd.read_json(jsonified_cleaned_data, orient='split')
        table = generate_table(dff)
        return table
    else:
        raise PreventUpdate

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

@app.callback(Output('graph1', 'figure'),
              Output('graph2', 'figure'),
              Output('graph3', 'figure'),
              Output('graph4', 'figure'),
              Output('users_unique_values', 'children'),
              Output('hashtags_wc', 'src'),
              Input('session', 'data'))
def render_graphs(jsonified_cleaned_data):
    files = glob.glob('assets/htwc/*')
    for f in files:
        os.remove(f)
    if jsonified_cleaned_data:
        dff = pd.read_json(jsonified_cleaned_data, orient='split')
        created_at = dff["Created_at"].apply(lambda x: x.date())

        fig1 = px.bar(dff, x=created_at.value_counts().keys(), y=created_at.value_counts().values,
                      labels={'x': 'Created at', 'y': "count"})

        fig2 = px.bar(dff, x=dff["location"].value_counts().keys(), y=dff["location"].value_counts().values,
                      labels={'x':'location', 'y': "count"})

        user_series = dff["source"].value_counts()
        tmp1 = user_series.loc[["Twitter for Android", "Twitter for iPhone", "Twitter Web App"]]
        tmp2 = user_series.drop(["Twitter for Android", "Twitter for iPhone", "Twitter Web App"])
        tmp1["Other"] = tmp2.sum()
        fig3 = px.bar(dff, x=tmp1.keys(), y=tmp1.values,
                      labels={'x':'source', 'y': "count"})

        fig4 = px.bar(dff, x=dff["retweet_count"].value_counts().keys(), y=dff["retweet_count"].value_counts().values,
                      labels={'x':'retweet_count', 'y': "count"})

        users = dff["user"].value_counts().size

        fname = generate_word_cloud(dff["hashtags"])

        return fig1, fig2, fig3, fig4, users, fname
    else:
        raise PreventUpdate


if __name__ == '__main__':
    app.run_server(debug=True, port=8052, dev_tools_hot_reload=False)

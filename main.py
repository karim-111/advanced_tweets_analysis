import os
import glob
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_extensions.snippets import send_data_frame

import pandas as pd
# Pages
from layouts import layout1
from Pages import Home_Page

# Callbacks
from Callbacks.maj_table import maj_table
from Callbacks.clean_tweet import clean_tweet
from Callbacks.sentiment_tweet import sentiment_tweet
from Callbacks.map_location import map_location
from Callbacks.figure_bilou import figure_bilou2
from Callbacks.call_api_search import call_api_search, call_api_search_by_name
from Callbacks.tree_tweets import tree_tweets
from Callbacks.FIgPca import PcaFirst
from Pages.SearchTweets import parse_contents
from Components.Table3 import generate_table2
#
from API.Cleaning_Tweets import df_with_clean_text
from API.Cleaning_Tweets import df_with_clean_text2
from API.Cleaning_Tweets import Give_The_Graph,Give_The_Graph_Word

#
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
len_data = 3500

app.layout = html.Div([
    # Save the tweets Searched by hashtag or name
    dcc.Store(id='session',
              data=[]),
    # Save the tweets Searched by the name of the owner of the count
    dcc.Store(id='session2',
              data=[]),
    dcc.Store(id='DataFrameUploaded',
              data=[]),
    # Save the Data Cleaned
    dcc.Store(id="clean_df",
              data=[]),
    dcc.Store(id="NMF_Topic_word",
              data=[]),
    # Save the Confusion Matrix
    dcc.Store(id="Confusion_Matrix",
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

    if pathname == '/':
        return Home_Page.layout


# Callback Pour la recherche des tweets
# Et enregistrement dans le dcc.store

@app.callback(
    Output('session', 'data'),
    Output('session2', 'data'),
    Output('ToHide', 'style'),
    Output('ToHide2', 'style'),
    Output("loading-output-1", "children"),
    Input('submit-button-state', 'n_clicks'),
    State('demo-dropdown', 'value'),
    State('my-input', 'value'),
    State('my-input-by-name', 'value'),

)
def update_output_div(n_clicks, number, input_value, inputtttt):
    if n_clicks is None:
        raise PreventUpdate
    else:
        if input_value != "":
            return call_api_search(input_value, number), [], {'display': 'none'}, {
                'display': 'flex'}, 'The tweets are succefuly loaded, navigate to Tab2 to see results'
        else:
            if inputtttt != "":
                return [], call_api_search_by_name(inputtttt), {'display': 'none'}, {
                    'display': 'flex'}, 'The tweets are succefuly loaded, navigate to Tab2 to see results'
            else:
                raise PreventUpdate


#
@app.callback(Output('NMF_Topic_word', 'data'), Input('session', 'data'),
              Input('session2', 'data'), Input('DataFrameUploaded', 'data'), Input("NumberOFTopic", 'value'))
def update_table_clean(jsonified_cleaned_data, jsonified_cleaned_data2, jsonified_cleaned_data3, n_topic):
    if jsonified_cleaned_data:
        if n_topic:
            return df_with_clean_text(jsonified_cleaned_data, n_topic)
        else:
            return df_with_clean_text(jsonified_cleaned_data, 2)
    else:
        if jsonified_cleaned_data2:
            if n_topic:
                return df_with_clean_text(jsonified_cleaned_data2, n_topic)
            else:
                return df_with_clean_text(jsonified_cleaned_data2, 2)

        else:
            if jsonified_cleaned_data3:
                if n_topic:
                    return df_with_clean_text(jsonified_cleaned_data3, n_topic)
                else:
                    return df_with_clean_text(jsonified_cleaned_data3, 2)
            else:
                raise PreventUpdate


## NMF

@app.callback(Output('NMF', 'figure'), Output('NMF2', 'figure'), Output('NMF3', 'figure'), Output('NMF4', 'figure'),
              Output('GaloupiNMF3', 'style'), Output('GaloupiNMF4', 'style'),

              Input("NumberOFTopic", 'value'),
              Input("NMF_Topic_word", 'data'))
def update_table_clean(numberOfTopics, jsonified_cleaned_data):
    if jsonified_cleaned_data:

        if numberOfTopics == 2:
            x, y = df_with_clean_text2(numberOfTopics, jsonified_cleaned_data)
            return x, y, {}, {}, {
                'display': 'none'}, {
                       'display': 'none'}
        else:
            if numberOfTopics == 3:
                x, y, z = df_with_clean_text2(numberOfTopics, jsonified_cleaned_data)
                return x, y, z, {}, {
                    'display': 'block'}, {
                           'display': 'none'}
            else:
                if numberOfTopics == 4:
                    x, y, z, w = df_with_clean_text2(numberOfTopics, jsonified_cleaned_data)

                    return x, y, z, w, {
                        'display': 'block'}, {
                               'display': 'block'},
    else:
        raise PreventUpdate


# Display Word And Topic Cosinus

@app.callback(Output('TopicCosinus', 'figure'),
              Input("NumberOFTopic", 'value'),
              Input("NMF_Topic_word", 'data'))
def update_table_clean(numberOfTopics, jsonified_cleaned_data):
    if jsonified_cleaned_data:
        fig = Give_The_Graph(numberOfTopics, jsonified_cleaned_data)
        return fig
    else:
        raise PreventUpdate


@app.callback(Output('WordCosinus', 'figure'),
              Input("TheTopicSelected", 'value'),
              Input("NMF_Topic_word", 'data'))
def update_table_clean(numberOfTopics, jsonified_cleaned_data):
    if jsonified_cleaned_data:
        fig = Give_The_Graph_Word(numberOfTopics, jsonified_cleaned_data)
        return fig
    else:
        raise PreventUpdate
##

## ACP
@app.callback( Output("Galoupi3", 'style'), Output("HideACP", 'style'),
              Input('NMF_Topic_word', 'data'))
def watwat(jsonified_cleaned_data):
    if jsonified_cleaned_data:
        return {'display': 'block'}, {'display': 'none'},
    else:
        raise PreventUpdate


@app.callback(Output('output-data-upload', 'children'),
              Output('DataFrameUploaded', 'data'),
              Output('HideDataFrame', 'style'),
              Output('Galoupi2', 'style'),
              Input('upload-data', 'contents'),
              Input('session', 'data'),
              Input('session2', 'data'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'),
              )
def update_output(list_of_contents, jsonified_cleaned_data, jsonified_cleaned_data2, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        print(children[0][1])

        return children[0][0], children[0][1].to_json(date_format='iso', orient='split'), {'display': 'none'}, {
            'display': 'flex'}
    else:
        if jsonified_cleaned_data:
            return generate_table2(jsonified_cleaned_data), [], {'display': 'none'}, {
                'display': 'flex'}
        else:
            if jsonified_cleaned_data2:
                return generate_table2(jsonified_cleaned_data2), [], {'display': 'none'}, {
                    'display': 'flex'}
            else:
                raise PreventUpdate


###
"""

@app.callback(Output('output-data-upload2', 'children'),
              Output('HideDataFrame', 'style'),
              Output('Galoupi2', 'style'),
              Input('session', 'data'),
              Input('session2', 'data'))
def update_output(jsonified_cleaned_data, jsonified_cleaned_data2):
    if jsonified_cleaned_data:
        return generate_table2(jsonified_cleaned_data), [], {'display': 'none'}, {
            'display': 'flex'}
    else:
        if jsonified_cleaned_data2:
            return generate_table2(jsonified_cleaned_data2), [], {'display': 'none'}, {
            'display': 'flex'}
        else:
            raise PreventUpdate
"""


##

# Cleaning the tweets and store it

@app.callback(Output('clean_df', 'data'), Input('session', 'data'),
              Input('session2', 'data'))
def update_table_clean(jsonified_cleaned_data, jsonified_cleaned_data2):
    if jsonified_cleaned_data:
        return clean_tweet(jsonified_cleaned_data)
    else:
        if jsonified_cleaned_data2:
            return clean_tweet(jsonified_cleaned_data2)
        else:
            return [], []


###
"""

@app.callback(Output('table', 'children'), Input('session', 'data'), Input('session2', 'data'))
def update_table(jsonified_cleaned_data, jsonified_cleaned_data2):
    if jsonified_cleaned_data:
        table = maj_table(jsonified_cleaned_data)
        return table
    else:
        if jsonified_cleaned_data2:
            table = maj_table(jsonified_cleaned_data2)
            return table
        else:
            raise PreventUpdate
"""


@app.callback(Output('tableTOSHow', 'children'),
              Input('session', 'data'),
              Input('session2', 'data'),
              Input('DataFrameUploaded', 'data'),
              )
def update_table_clean(jsonified_cleaned_data, jsonified_cleaned_data2, jsonified_cleaned_data3):
    if jsonified_cleaned_data:
        return tree_tweets(jsonified_cleaned_data)
    else:
        if jsonified_cleaned_data2:
            return tree_tweets(jsonified_cleaned_data2)
        else:
            if jsonified_cleaned_data3:
                return tree_tweets(jsonified_cleaned_data3)

            else:
                return []


# sentiment analyses
@app.callback(Output('idee', 'figure'), Input('session', 'data'), Input('session2', 'data'),
              Input('DataFrameUploaded', 'data'))
def watwat(jsonified_cleaned_data, jsonified_cleaned_data2, jsonified_cleaned_data3):
    if jsonified_cleaned_data:
        return sentiment_tweet(jsonified_cleaned_data)
    else:
        if jsonified_cleaned_data2:
            return sentiment_tweet(jsonified_cleaned_data2)
        else:
            if jsonified_cleaned_data3:
                return sentiment_tweet(jsonified_cleaned_data3)
            else:
                raise PreventUpdate


@app.callback(Output("download", "data"), Input("btn", "n_clicks"), Input('session', 'data'), Input('session2', 'data'),
              Input('DataFrameUploaded', 'data'))
def generate_csv(n_clicks, jsonified_cleaned_data, jsonified_cleaned_data2, jsonified_cleaned_data3):
    if n_clicks is None:
        raise PreventUpdate
    else:
        if jsonified_cleaned_data:
            df = pd.read_json(jsonified_cleaned_data, orient='split')

            return send_data_frame(df.to_csv, filename="some_name.csv")
        else:
            if jsonified_cleaned_data2:
                df = pd.read_json(jsonified_cleaned_data2, orient='split')
                return send_data_frame(df.to_csv, filename="some_name.csv")
            else:
                if jsonified_cleaned_data3:
                    df = pd.read_json(jsonified_cleaned_data3, orient='split')
                    return send_data_frame(df.to_csv, filename="some_name.csv")
                else:
                    raise PreventUpdate


# Map Location
@app.callback(Output('Map', 'figure'), Output('theBigOne', 'style'),
              Output('englobanteToHide2', 'style'), Output('ToShow', 'style'), Input('session', 'data'),
              Input('session2', 'data'), Input('DataFrameUploaded', 'data'))
def watwat(jsonified_cleaned_data, jsonified_cleaned_data2, jsonified_cleaned_data3):
    if jsonified_cleaned_data:
        return map_location(jsonified_cleaned_data), {'display': 'block'}, {'display': 'none'}, {'display': 'flex'}
    else:
        if jsonified_cleaned_data2:
            return map_location(jsonified_cleaned_data2), {'display': 'block'}, {'display': 'none'}, {'display': 'flex'}
        else:
            if jsonified_cleaned_data3:
                return map_location(jsonified_cleaned_data3), {'display': 'block'}, {'display': 'none'}, {
                    'display': 'flex'}

            else:
                raise PreventUpdate


@app.callback(Output('hashtags_wc', 'src'),
              Input('session', 'data'),
              Input('session2', 'data'),
              Input('DataFrameUploaded', 'data')
              )
def render_graphs(jsonified_cleaned_data, jsonified_cleaned_data2, jsonified_cleaned_data3):
    files = glob.glob('assets/htwc/*')
    for f in files:
        os.remove(f)
    if jsonified_cleaned_data:
        return figure_bilou2(jsonified_cleaned_data)
    else:
        if jsonified_cleaned_data2:
            return figure_bilou2(jsonified_cleaned_data2)
        else:
            if jsonified_cleaned_data3:
                return figure_bilou2(jsonified_cleaned_data3)
            else:
                raise PreventUpdate


if __name__ == '__main__':
    app.run_server(debug=True, port=8052, dev_tools_hot_reload=False)

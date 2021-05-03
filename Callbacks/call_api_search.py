import pandas as pd
from dash.exceptions import PreventUpdate
from API.Scraping_Tweets import search
from API.Scraping_Tweets import search_by_name


def call_api_search(input_value, number):
    df = search(input_value, number)
    return df.to_json(date_format='iso', orient='split')


def call_api_search_by_name(input_value):
    df = search_by_name(input_value)
    return df.to_json(date_format='iso', orient='split')

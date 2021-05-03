import pandas as pd
import plotly.express as px
from API.Utils import generate_word_cloud


def figure_bilou2(data):
    dff = pd.read_json(data, orient='split')
    fname = generate_word_cloud(dff["hashtags"])

    return fname

import pandas as pd
import folium
from API.GetMap import put_markers


def map_location(data):
    df = pd.read_json(data, orient='split')
    df = df[['user', 'location']]
    df = df.values.tolist()

    map = folium.Map(location=[0, 0], zoom_start=2)
    fig = put_markers(map, df)
    return fig

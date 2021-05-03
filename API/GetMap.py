import folium
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import pandas as pd
import plotly.express as px


def put_markers(map, data):
    geo_locator = Nominatim(user_agent="LearnPython")
    df2 = pd.DataFrame([['karim', 48.856614, 2.3522219]], columns=['user', 'lat', 'long'])
    for (name, location) in data:
        if location:
            try:
                #print(location)

                location = geo_locator.geocode(location, timeout=None)
            except GeocoderTimedOut as e:
                print("Error: geocode failed on input %s with message %s" % (location, e.message))
                continue
            if location:
                df3 = pd.DataFrame([[name, location.latitude, location.longitude]], columns=['user', 'lat', 'long'])
                df2 = df2.append(df3, ignore_index=True)
                #print(df2)

    fig = px.scatter_mapbox(df2, lat="lat", lon="long", hover_name="user",
                            color_discrete_sequence=["blue"], zoom=1, height=500)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 1, "t": 1, "l": 1, "b": 1})
    return fig

import plotly.express as px
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
from dash.exceptions import PreventUpdate




def PcaFirst(data):
    df = pd.read_json(data, orient='split')

    pca = PCA(n_components=2)
    components = pca.fit_transform(df)

    fig = px.scatter(components, color=df['Topic'],
                     x=0, y=1)
    return fig






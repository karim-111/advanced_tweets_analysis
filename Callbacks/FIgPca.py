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



def Pour_Com(data):
    df = pd.read_json(data, orient='split')
    pca = PCA()
    pca.fit(df)
    exp_var_cumul = np.cumsum(pca.explained_variance_ratio_)

    return px.area(
        x=range(1, exp_var_cumul.shape[0] + 1),
        y=exp_var_cumul,
        labels={"x": "# Components", "y": "Explained Variance"}
    )


def PCA3D(data):
    df = pd.read_json(data, orient='split')
    pca = PCA(n_components=3)
    components = pca.fit_transform(df)

    total_var = pca.explained_variance_ratio_.sum() * 100

    fig = px.scatter_3d(
        components, x=0, y=1, z=2,
        color=df['Topic'],

        title=f'Total Explained Variance: {total_var:.2f}%',
        labels={'0': 'PC 1', '1': 'PC 2', '2': 'PC 3'}
    )
    return fig
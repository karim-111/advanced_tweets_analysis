import dash_core_components as dcc
import dash_html_components as html
from dash_extensions import Download

import dash_bootstrap_components as dbc

tab4_content = html.Div(
    className="etoite",
    children=[
        html.Div(
            id ="Galoupi2",
            className="ToDisplayDataFrame",

            children=[
                html.Div([html.Button("Download csv", id="btn",  className="hhhhhhhhhhhZ"), Download(id="download")]),
                html.Div(id='output-data-upload'),
                html.Div(id='output-data-upload2'),

            ]
        ),
        html.Div(
            id="HideDataFrame",
            style={'display': 'block'},
            children=[
                html.Img(className="hhh", src=("/assets/Nodata.jpg")),
            ]
        )]
),

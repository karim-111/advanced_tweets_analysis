import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

tab3_content = html.Div(
children=[
    html.Div(
        className='Galoupi',
        children=[
            dcc.Graph(id="Pourcentage_DES_composantes"),
            dcc.Graph(id="ACP"),
            html.Button(id = "maybe",children=("clickMe")),
            dcc.Graph(id="ACPTREED"),

        ]
    )]
),



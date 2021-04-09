import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc



tab2_content = html.Div(
    html.Div(
        [
            html.Div(id='jecpas'),
            dcc.Graph(id="idee"),

            dcc.Graph(id="graph1"),
            dcc.Graph(id="graph2"),
            dcc.Graph(id="graph3"),
            dcc.Graph(id="graph4"),
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("Users:", className="card-title"),
                        html.P([
                            html.Div(id="users_unique_values"),
                            "Unique values"
                        ],
                            className="card-text",
                        )
                    ]
                ),
                style={"width": "18rem", "margin": "10em"},
            ),
            html.Img(id="hashtags_wc")

        ]
    ),
    className="mt-3",
)


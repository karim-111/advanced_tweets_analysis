import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc



tab2_content = html.Div(
    html.Div(
        [

            dcc.Graph(id="graph1"),
            dcc.Graph(id="graph2"),
            dcc.Graph(id="graph3"),
            dcc.Graph(id="graph4"),
            dcc.Graph(id="graph5"),

        ]
    ),
    className="mt-3",
)


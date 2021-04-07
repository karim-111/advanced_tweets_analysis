import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc



tab2_content = html.Div(
    html.Div(
        [
            dcc.Graph(id="graph"),

        ]
    ),
    className="mt-3",
)


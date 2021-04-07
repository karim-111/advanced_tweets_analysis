import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # This is the 'hidden div' however its really a container for sub-divs, some hidden, some not
    html.Div(id='output-data-upload', style={'display': 'none'}),
    html.Br(),
    html.Div(id='page-content')
])
server = app.server

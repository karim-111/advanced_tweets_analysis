import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from Pages.SearchTweets import tab1_content
from Pages.Visualisation_Tweets import tab2_content
from Components import NavBar
layout1 = html.Div([
NavBar.navbar,
dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Search tweets",tabClassName="TabStyle"),
        dbc.Tab(tab2_content, label="Visualize data", tabClassName="TabStyle"),


    ]
),



])


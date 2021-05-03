import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from Pages.SearchTweets import tab1_content
from Pages.Visualisation_Tweets import tab2_content
from Pages.NonSup import tab3_content
from Pages.DataFrame import tab4_content
from Components import NavBar

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

layout1 = html.Div([
    NavBar.navbar,
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(tab1_content, label='Search Tweets', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(tab2_content, label='Data visualisation', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(tab3_content, label='Topic Modeling', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(tab4_content, label='Data table', value='tab-4', style=tab_style,selected_style=tab_selected_style),

    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
])


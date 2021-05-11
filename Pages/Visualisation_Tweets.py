import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

tab2_content = html.Div(
    id='theBigOne',
    className='Tab2Content',
    children=[
        html.Div(
            id='ToHide',
            style={'display': 'flex'},
            children=[
                html.Img(className="hhhh", src=("/assets/4689040.jpg")),
            ]
        ),
        html.Div(
            id="englobanteToHide2",
            style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'justifyContent': 'center'},
            children=[
                html.Div(
                    id='ToHide2',
                    style={'display': 'none', 'flexDirection': 'column', 'alignItems': 'center'},
                    children=[
                        html.H1('Please wait it will take a few seconds ...'),
                        dbc.Spinner(color="primary", spinner_style={"width": "10rem", "height": "3rem"}),

                    ]
                ),
            ]
        ),

        html.Div(
            id='ToShow',
            className='Tab2Content2',
            children=[
                html.H1("1. Sentiment analysis ", style={"marginTop": "30px", "color": "blue"}),
                html.Div(
                    className='Galoupi',
                    children=[
                        dcc.Graph(id="idee")]
                ),
                html.H1("2. Location ", style={"color": "blue"}),
                html.Div(
                    className='Galoupi',
                    children=[dcc.Graph(id="Map")]
                ),

                html.H1("3. World Cloud  ", style={"marginBottom": "30px", "color": "blue"}),

                html.Img(id="hashtags_wc"),
                html.Img(id="hashtags_wc2"),
                html.H1("", style={"marginBottom": "50px"}),
                html.H1("4. Top 3 tweets retweeted  ", style={"marginBottom": "30px", "color": "blue"}),

                html.Div(id="tableTOSHow"),
                html.H1("", style={"marginBottom": "30px"}),

            ]
        )]
)

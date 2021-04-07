import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div(
    className="first",

    children=[
        html.Div(
            className="LogoAndTitle",
            children=[
                html.Img(className="hh", src=("/assets/Logo.png")),
                html.H1(children=" TweeMusk", className='titre'),
            ]
        ),
        html.Div(
            className="second",

            children=[
                html.Div(
                    className='trrrrr',
                    children=[

                        html.Div(
                            className="formulaire",
                            children=[
                                html.P(
                                    className='theParagraph',
                                    children=["TweeMusk is an online tool that allows you to retrieve and     "
                                              "analyze tweets in real time, you just have to put your request and then visualize the result."]
                                ),
                                html.Div(
                                    className="inputAndSubmit",
                                    children=[
                                        html.A(html.Button('Begin Now', className='hhhhhhhhhhh'),
                                               href='/login'),

                                    ]),

                            ]
                        ),

                    ]
                ),

                html.Br(),
                html.Div(id='intermediate-value', style={'display': 'none'}),
                html.Div(id="hk")

            ])

    ])

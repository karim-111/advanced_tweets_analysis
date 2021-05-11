import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

tab3_content = html.Div(
    className='Tab3Content',

    children=[
        html.Div(
            id="Galoupi3",
            className="EnglobTwoBlock",
            children=[
                html.Div(
                    className="FirstFirstBlock",
                    children=[
                        html.Div(
                            className="NchedInput",
                            children=[
                                html.H1(style={"marginBottom": "20px"}, children=("Topic Modeling")),
                                html.Div(
                                    children=[
                                        dcc.Dropdown(id="NumberOFTopic",
                                                     options=[
                                                         {'label': '2 Topics', 'value': 2},
                                                         {'label': '3 Topics', 'value': 3},
                                                         {'label': '4 Topics ', 'value': 4},

                                                     ],
                                                     value=2
                                                     ),
                                    ]
                                ),
                            ]
                        ),
                        html.Div(
                            className="FirstBlock",
                            children=[

                                html.Div(
                                    className='Galoupi',
                                    children=[
                                        dcc.Graph(id="NMF")
                                    ]
                                ),
                                html.Div(
                                    className='GaloupiNMF2',
                                    children=[
                                        dcc.Graph(id="NMF2")
                                    ]
                                ),
                                html.Div(
                                    id="GaloupiNMF3",

                                    className='GaloupiNMF3',
                                    children=[
                                        dcc.Graph(id="NMF3")
                                    ]
                                ),
                                html.Div(
                                    id="GaloupiNMF4",
                                    className='GaloupiNMF4',
                                    children=[
                                        dcc.Graph(id="NMF4")
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
                html.Div(
                  className="SecondSecondBlock",
                  children=[
                      html.Div(
                          className="NchedInput",
                          children=[
                              html.Div(
                                  children=[
                                      dcc.Dropdown(id="TheTopicSelected",
                                                   options=[
                                                       {'label': 'Topic 1', 'value': 1},
                                                       {'label': 'Topic 2', 'value': 2},
                                                       {'label': 'Topic 3 ', 'value': 3},

                                                   ],
                                                   value=1
                                                   ),
                                  ]
                              ),
                          ]
                      ),
                      html.Div(
                          className="SecondBlock",
                          children=[

                              html.Div(
                                  id="Ga",
                                  className='Galoupi',
                                  children=[
                                      dcc.Graph(id="TopicCosinus")
                                  ]
                              ),
                              html.Div(
                                  id="WordCosinus",
                                  className='Galoupi',
                                  children=[
                                      dcc.Graph(id="WordCosinus")
                                  ]
                              ),

                          ]
                      ),

                  ]
                ),



            ]
        ),

        html.Div(
            id="HideACP",
            style={'display': 'block'},
            children=[
                html.Img(className="hhh", src=("/assets/ML.jpg")),
            ]
        )

    ]
),

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table


def generate_table(dataframe):
    return dash_table.DataTable(
        id='table',
        style_table={'overflowX': 'auto'},
        style_cell={
            'height': 'auto',
            # all three widths are needed
            'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
            'whiteSpace': 'normal'
        },
        columns=[
            {"name": i, "id": i} for i in sorted(dataframe.columns)
        ],
        page_current=0,
        page_size=5,
        page_action='custom',
        data=dataframe.to_dict('records'),

    )

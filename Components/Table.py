import dash_html_components as html
import dash_bootstrap_components as dbc


def generate_table(dataframe, max_rows=5):
    df = dataframe[:10]
    return  dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
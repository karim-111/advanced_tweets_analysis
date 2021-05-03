from Components.Table import generate_table
import pandas as pd
from itables import init_notebook_mode
from itables import show

def maj_table(data) :
    if data:
        dff = pd.read_json(data, orient='split')
        table = generate_table(dff)
        return table
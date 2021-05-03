import pandas as pd
from Components.Table import generate_table
from API.Cleaning_Tweets import clean

def clean_tweet(data) :
    df = pd.read_json(data, orient='split')
    df['Text'] = df['Text'].apply(clean)
    table = generate_table(df)
    return table, df.to_json(date_format='iso', orient='split')
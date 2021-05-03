import pandas as pd
from Components.Table import generate_table


def tree_tweets(data):
    df = pd.read_json(data, orient='split')
    elderly = df.nlargest(3, 'retweet_count')
    elderly2 = elderly[["Text", "retweet_count"]]
    print(elderly2)
    table = generate_table(elderly2)
    return table

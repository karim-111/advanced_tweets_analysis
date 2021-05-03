from API.Sentiment_analyse import getAnalysis, getPolarity, getSubjectivity
import pandas as pd
import plotly.express as px
from collections import Counter


def sentiment_tweet(data):
    df = pd.read_json(data, orient='split')

    df['subjectivity'] = df['Text'].apply(getSubjectivity)
    df['polarity'] = df['Text'].apply(getPolarity)
    df['analysis'] = df['polarity'].apply(getAnalysis)

    target_cnt = Counter(df.analysis)
    df2 = pd.DataFrame.from_dict(target_cnt, orient='index').reset_index()
    df2.columns = ['value', 'key']
    df2
    fig = px.bar(df2, x='value', y='key', labels={'x': 'total_bill', 'y': 'count'})

    return fig

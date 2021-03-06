import re
import string
import plotly.express as px
import nltk
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

wn = nltk.WordNetLemmatizer()

stopword = nltk.corpus.stopwords.words('english')


def clean(text):
    tweet = str(text).lower()
    tweet = re.sub('\[.*?\_]', '', tweet)
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)  # Remove http links
    tweet = re.sub('<.*?>+', '', tweet)

    tweet = re.sub('\n', '', tweet)
    tweet = re.sub('\w*\d\w*', '', tweet)
    tweet = re.sub(r'@[A-Za-z0-9]+', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    tweet = re.sub(r'RT[\s]+', '', tweet)
    tweet = re.sub(r'[^\w]', ' ', tweet)
    tweet = re.sub('https*', '', tweet)

    tweet = re.sub(r"he's", "he is", tweet)
    tweet = re.sub(r"dont", "do not", tweet)
    tweet = re.sub(r"there's", "there is", tweet)
    tweet = re.sub(r"We're", "We are", tweet)
    tweet = re.sub(r"That's", "That is", tweet)
    tweet = re.sub(r"won't", "will not", tweet)
    tweet = re.sub(r"they're", "they are", tweet)
    tweet = re.sub(r"Can't", "Cannot", tweet)
    tweet = re.sub(r"wasn't", "was not", tweet)
    tweet = re.sub(r"don\x89Ûªt", "do not", tweet)
    tweet = re.sub(r"aren't", "are not", tweet)
    tweet = re.sub(r"isn't", "is not", tweet)
    tweet = re.sub(r"What's", "What is", tweet)
    tweet = re.sub(r"haven't", "have not", tweet)
    tweet = re.sub(r"hasn't", "has not", tweet)
    tweet = re.sub(r"There's", "There is", tweet)
    tweet = re.sub(r"He's", "He is", tweet)
    tweet = re.sub(r"It's", "It is", tweet)
    tweet = re.sub(r"You're", "You are", tweet)
    tweet = re.sub(r"I'M", "I am", tweet)
    tweet = re.sub(r"shouldn't", "should not", tweet)
    tweet = re.sub(r"wouldn't", "would not", tweet)
    tweet = re.sub(r"i'm", "I am", tweet)
    tweet = re.sub(r"I\x89Ûªm", "I am", tweet)
    tweet = re.sub(r"I'm", "I am", tweet)
    tweet = re.sub(r"Isn't", "is not", tweet)
    tweet = re.sub(r"Here's", "Here is", tweet)
    tweet = re.sub(r"you've", "you have", tweet)
    tweet = re.sub(r"you\x89Ûªve", "you have", tweet)
    tweet = re.sub(r"we're", "we are", tweet)
    tweet = re.sub(r"what's", "what is", tweet)
    tweet = re.sub(r"couldn't", "could not", tweet)
    tweet = re.sub(r"we've", "we have", tweet)
    tweet = re.sub(r"it\x89Ûªs", "it is", tweet)
    tweet = re.sub(r"doesn\x89Ûªt", "does not", tweet)
    tweet = re.sub(r"It\x89Ûªs", "It is", tweet)
    tweet = re.sub(r"Here\x89Ûªs", "Here is", tweet)
    tweet = re.sub(r"who's", "who is", tweet)
    tweet = re.sub(r"I\x89Ûªve", "I have", tweet)
    tweet = re.sub(r"y'all", "you all", tweet)
    tweet = re.sub(r"can\x89Ûªt", "cannot", tweet)
    tweet = re.sub(r"would've", "would have", tweet)
    tweet = re.sub(r"it'll", "it will", tweet)
    tweet = re.sub(r"we'll", "we will", tweet)
    tweet = re.sub(r"wouldn\x89Ûªt", "would not", tweet)
    tweet = re.sub(r"We've", "We have", tweet)
    tweet = re.sub(r"he'll", "he will", tweet)
    tweet = re.sub(r"Y'all", "You all", tweet)
    tweet = re.sub(r"Weren't", "Were not", tweet)
    tweet = re.sub(r"Didn't", "Did not", tweet)
    tweet = re.sub(r"they'll", "they will", tweet)
    tweet = re.sub(r"they'd", "they would", tweet)
    tweet = re.sub(r"DON'T", "DO NOT", tweet)
    tweet = re.sub(r"That\x89Ûªs", "That is", tweet)
    tweet = re.sub(r"they've", "they have", tweet)
    tweet = re.sub(r"i'd", "I would", tweet)
    tweet = re.sub(r"should've", "should have", tweet)
    tweet = re.sub(r"You\x89Ûªre", "You are", tweet)
    tweet = re.sub(r"where's", "where is", tweet)
    tweet = re.sub(r"Don\x89Ûªt", "Do not", tweet)
    tweet = re.sub(r"we'd", "we would", tweet)
    tweet = re.sub(r"i'll", "I will", tweet)
    tweet = re.sub(r"weren't", "were not", tweet)
    tweet = re.sub(r"They're", "They are", tweet)
    tweet = re.sub(r"Can\x89Ûªt", "Cannot", tweet)
    tweet = re.sub(r"you\x89Ûªll", "you will", tweet)
    tweet = re.sub(r"I\x89Ûªd", "I would", tweet)
    tweet = re.sub(r"let's", "let us", tweet)
    tweet = re.sub(r"it's", "it is", tweet)
    tweet = re.sub(r"can't", "cannot", tweet)
    tweet = re.sub(r"don't", "do not", tweet)
    tweet = re.sub(r"you're", "you are", tweet)
    tweet = re.sub(r"i've", "I have", tweet)
    tweet = re.sub(r"that's", "that is", tweet)
    tweet = re.sub(r"i'll", "I will", tweet)
    tweet = re.sub(r"doesn't", "does not", tweet)
    tweet = re.sub(r"i'd", "I would", tweet)
    tweet = re.sub(r"didn't", "did not", tweet)
    tweet = re.sub(r"ain't", "am not", tweet)
    tweet = re.sub(r"you'll", "you will", tweet)
    tweet = re.sub(r"I've", "I have", tweet)
    tweet = re.sub(r"Don't", "do not", tweet)
    tweet = re.sub(r"I'll", "I will", tweet)
    tweet = re.sub(r"I'd", "I would", tweet)
    tweet = re.sub(r"Let's", "Let us", tweet)
    tweet = re.sub(r"you'd", "You would", tweet)
    tweet = re.sub(r"It's", "It is", tweet)
    tweet = re.sub(r"Ain't", "am not", tweet)
    tweet = re.sub(r"Haven't", "Have not", tweet)
    tweet = re.sub(r"Could've", "Could have", tweet)
    tweet = re.sub(r"youve", "you have", tweet)
    tweet = re.sub(r"donå«t", "do not", tweet)
    return tweet


def clean_text2(text):
    text_wtu = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())
    text_rc = re.sub('[0-9]+', '', text_wtu)
    text_wat = clean(text_rc)
    text_lem = wn.lemmatize(text_wat)
    return text_lem


def df_with_clean_text(data, number):
    df = pd.read_json(data, orient='split')
    df['clean_text'] = df['Text'].apply(lambda x: clean_text2(x))
    df
    # use tfidf by removing tokens that don't appear in at least 50 documents
    vect = TfidfVectorizer(min_df=3, stop_words='english')
    X = vect.fit_transform(df.clean_text)
    # NMF
    model = NMF(n_components=number, random_state=5)

    # Fit the model to TF-IDF
    model.fit(X)

    components_df = pd.DataFrame(model.components_, columns=vect.get_feature_names())
    print(components_df)
    Topic = []
    for i in range(number):
        Topic.append(i + 1)
    Topic

    components_df["Topic"] = Topic
    return components_df.to_json(date_format='iso', orient='split')


def df_with_clean_text2(numberofboucle, data):
    components_df = pd.read_json(data, orient='split')

    # index = components_df.index
    # number_of_rows = len(index)

    def watttt(b):
        # print('b',b)
        # print("componenet",components_df)

        H2 = components_df.iloc[b - 1]
        # print('H2',H2)

        H2 = pd.DataFrame(H2)
        H3 = H2.nlargest(20, b - 1)
        # print('H3',H3)

        return H3

    if numberofboucle == 2:
        return px.bar(watttt(1)), px.bar(watttt(2))
    else:
        if numberofboucle == 3:
            return px.bar(watttt(1)), px.bar(watttt(2)), px.bar(watttt(3))
        else:
            if numberofboucle == 4:
                return px.bar(watttt(1)), px.bar(watttt(2)), px.bar(watttt(3)), px.bar(watttt(4))


####
def word2vec(word):
    from collections import Counter
    from math import sqrt

    # count the characters in word
    cw = Counter(word)
    # precomputes a set of the different characters
    sw = set(cw)
    # precomputes the "length" of the word vector
    lw = sqrt(sum(c * c for c in cw.values()))

    # return a tuple
    return cw, sw, lw


def cosdis(v1, v2):
    # which characters are common to the two words?
    common = v1[1].intersection(v2[1])
    # by definition of cosine distance we have
    return sum(v1[0][ch] * v2[0][ch] for ch in common) / v1[2] / v2[2]


####
def Give_The_Graph(numbertoboucle, data):
    components_df = pd.read_json(data, orient='split')
    csim = cosine_similarity(components_df, components_df)
    docList = []
    for i in range(1, numbertoboucle + 1):
        docList.append("Topic " + str(i))
    print("dockccc", docList)
    csimDf = pd.DataFrame(csim, index=sorted(docList), columns=sorted(docList))
    csimDf = csimDf.values.tolist()
    data = csimDf
    print('data', data)
    fig = px.imshow(data,
                    labels=dict(x="Topic", y="Topic", color="Productivity"),
                    x=docList,
                    y=docList,
                    )
    fig.update_xaxes(side="top")
    return fig
####
def Give_The_Graph_Word(number, data):
    components_df = pd.read_json(data, orient='split')
    H2 = components_df.iloc[number]
    H2 = pd.DataFrame(H2)
    H3 = H2.nlargest(20, number)
    index = H3.index
    index = index.tolist()
    data = []
    for i in index:
        data.append(word2vec(i))
    res = [[0 for i in range(len(index))] for j in range(len(index))]
    for i in range(0, 19):
        for j in range(0, 19):
            wat = cosdis(data[i], data[j])
            res[i][j] = wat

    df = pd.DataFrame(res)
    df
    wat = df.values.tolist()
    data = wat
    fig = px.imshow(data,
                    labels=dict(x="Topic", y="Topic", color="Productivity"),
                    x=index,
                    y=index,
                    )
    fig.update_xaxes(side="top")

    return fig


""""
    if number_of_rows <number+1 :
        H2 = components_df.iloc[number_of_rows -1]
        H2 = pd.DataFrame(H2)
        H3 = H2.nlargest(20,number_of_rows -1)
    else :
        H2 = components_df.iloc[number]
        H2 = pd.DataFrame(H2)
        H3 = H2.nlargest(20, number)
    """

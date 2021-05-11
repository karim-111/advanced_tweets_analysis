import re
from wordcloud import WordCloud
import time


def generate_word_cloud(column):
    text = " ".join([str(hashtag) for hashtag in column])
    #matched = re.match("[a-z][0-9][a-z][0-9]+", text)
    boll = False
    #is_match = bool(matched)
    #print("is_match",is_match)
    #print("text",text)
    word = "e"
    if word in text:
        boll = True
    if boll:
        wordcloud = WordCloud(background_color='white', max_words=50, width=1000, height=500,
                              collocations=False).generate(text)
        filename = ".".join([hex(int(time.time())), "png"])
        wordcloud.to_file("assets/htwc/{}".format(filename))
        return "assets/htwc/{}".format(filename)
    else:
        text = "No_Hashtags"
        wordcloud = WordCloud(background_color='white', max_words=50, width=1000, height=500,
                              collocations=False).generate(text)
        filename = ".".join([hex(int(time.time())), "png"])
        wordcloud.to_file("assets/htwc/{}".format(filename))
        return "assets/htwc/{}".format(filename)

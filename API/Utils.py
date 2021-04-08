
from wordcloud import WordCloud
import time


def generate_word_cloud(column):
    text = " ".join([hashtag for hashtag in column])
    wordcloud = WordCloud(background_color='white', max_words=50, width=1000, height=500, collocations=False).generate(text)
    filename=".".join([hex(int(time.time())),"png"])
    wordcloud.to_file("assets/htwc/{}".format(filename))
    return "assets/htwc/{}".format(filename)

import tweepy as tweepy
import pandas as pd
import csv

consumer_key = "VBekhUci4cmMhv0iGzUNFjnnb"
consumer_secret = "qDufneiJsdzoRYLWF2dbXNgLGwRyVZFoeK034stRk6cbxQh30d"
access_key = "1365352224642244618-mdWcSB2ZJLod3FcGwWqxPfhJ6Gvi8n"
access_secret = "ahBQ9t2IVlFlQORSE2FBcJq1eZEhsPnd1MV3BYLOoTHch"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def search(word):
    if word != "":
        search_words = word
        new_search = search_words + "-filter:retweets"
        date_since = "2020-03-15"

        tweets = tweepy.Cursor(api.search,
                               q=new_search,
                               lang="en",
                               since=date_since).items(100)

        # Collect a list of tweets
        users_locs = [[tweet.created_at,
                       tweet.text,
                       tweet.user.screen_name,
                       " ".join([hashtag['text'] for hashtag in tweet.entities['hashtags']]),
                       tweet.user.location,
                       tweet.source,
                       tweet.retweet_count]
                      for
                      tweet in tweets]
        df = pd.DataFrame(data=users_locs,
                          columns=['Created_at', 'Text', 'user', 'hashtags', 'location', 'source', 'retweet_count'])

        return df

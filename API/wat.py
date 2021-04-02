import tweepy as tweepy
import pandas as pd
import csv

consumer_key = "BMVUqJjofnBe96xevCJN1lVK3"
consumer_secret = "QAocQ0cCLdf6yNSYU5sVpUxBP7Ym4OY9nRHy6zi9kuxQuOsgOx"
access_key = "1365352224642244618-4EZsVnKrAnybcUiMxUaTy19gVT0gbv"
access_secret = "sTsXxrAijHlzoioYL72RUhY8xqtbygK0ydGNHrU44i9uM"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def search(word):
    if word != "" :
         search_words = word
         new_search = search_words + "-filter:retweets"
         date_since = "2020-03-15"

         tweets = tweepy.Cursor(api.search,
                           q=new_search,
                           lang="en",
                           since=date_since).items(105)

          # Collect a list of tweets
         users_locs = [[tweet.created_at, tweet.text, tweet.user.screen_name, tweet.user.location, tweet.retweet_count] for
                         tweet in tweets]
         df = pd.DataFrame(data=users_locs,
                      columns=['Created_at', 'Text', 'user', 'location', 'retweet_count'])

         return df

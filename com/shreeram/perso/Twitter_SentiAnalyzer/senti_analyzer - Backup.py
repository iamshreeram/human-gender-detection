################################################
################################################
# TITLE     : SENTIMENT ANALYZER FOR TWEETS
# AUTHOR    : SHREERAM VAIDHYANATHAN
# LICENCED  : APACHE
################################################
################################################

from textblob import TextBlob
import tweepy

cons_key = 's9uPtAY1McghyALKKQuxyKQlV'
cons_sec = 'kSisXo1B1QAjrvxyeaobMi7q6f0jvzFDJtePMxEGeeSt1RNmBK'
acces_tk = '222158291-12wkWBZnkZOK9ELjQHMzt724px4xm7blN8QUTXNt'
acces_tk_sec = '5kyY86cL9FzTqBWL3ucbO3CgaZIppjQTcHNHIX5Jw8Xq3'

auth = tweepy.OAuthHandler(cons_key,cons_sec)
auth.set_access_token(acces_tk,acces_tk_sec)

api = tweepy.API(auth)


tweets = api.search('Trump')

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)


public_tweets = api.home_timeline()

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    print analysis, analysis.sentiment

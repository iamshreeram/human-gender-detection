import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 's9uPtAY1McghyALKKQuxyKQlV'
consumer_secret = 'kSisXo1B1QAjrvxyeaobMi7q6f0jvzFDJtePMxEGeeSt1RNmBK'
access_token = '222158291-12wkWBZnkZOK9ELjQHMzt724px4xm7blN8QUTXNt'
access_token_secret = '5kyY86cL9FzTqBWL3ucbO3CgaZIppjQTcHNHIX5Jw8Xq3'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    print "Entering main program"
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets for #programming:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['trump'])

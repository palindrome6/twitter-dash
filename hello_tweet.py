import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from misc_functions import *

key_dict = get_keys()

consumer_key = key_dict['consumer_key']
consumer_secret = key_dict['consumer_secret']
access_token = key_dict['access_token']
access_secret = key_dict['access_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            # with open('python.json', 'a') as f:
            #     f.write(data)
            #     return True
            print(data)

        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['arsenal'])

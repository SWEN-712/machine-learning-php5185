from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import re, string, unicodedata

consumer_key = "vdIBAWroPAtq8LLVZzJNUZEU2"  # twitter app’s API Key
consumer_secret = "BAwl6FV70lVUZpxXubCELKwYvW4k3cROQIjiRujJU0gl3381er"  # twitter app’s API secret Key
access_token = "970899823-19IZbxq6mIWJlbvc9uabpfijaY3IEmR7I7YnJ2W9"  # twitter app’s Access token
access_token_secret = "ypmGfnCNTdi68oEnqTFijZ60HSwigLqbAHsczY3AARGCw"  # twitter app’s access token secret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

trump_tweets = auth_api.user_timeline(screen_name='DisabilityIN', count=5, include_rts=True, tweet_mode='extended')

final_tweets = [each_tweet.full_text for each_tweet in trump_tweets]
with open('DisabilityIn.txt', 'w') as f:
    for item in final_tweets:
        item = re.sub(r"http\S+", "", item)#removes urls
        f.write("%s\n" % item)

read_tweets = []
with open('DisabilityIn.txt', 'r') as f:
    read_tweets.append(f.read())

for x in read_tweets:
    print(x)

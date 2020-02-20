import tweepy
import re, string, unicodedata

# import pandas as pd
####input your credentials here
# consumer_key = ''
# consumer_secret = ''
# access_token = ''
# access_token_secret = ''

consumer_key = "vdIBAWroPAtq8LLVZzJNUZEU2"  # twitter app’s API Key
consumer_secret = "BAwl6FV70lVUZpxXubCELKwYvW4k3cROQIjiRujJU0gl3381er"  # twitter app’s API secret Key
access_token = "970899823-59PL3ambncjBsFjPaGJgNRmiX2yyBEA4N8SJZxqb"  # twitter app’s Access token
access_token_secret = "U6i2EBXZRmuFfdXChHBXBTq9k4jDe60nf7Is2UXDbQ5wE"  # twitter app’s access token secret


def getTweets():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    #####United Airlines
    # Open/Create a file to append data
    # csvFile = open('ua.csv', 'a')
    # Use csv Writer
    # csvWriter = csv.writer(csvFile)
    list = set()
    count =0

    get = tweepy.Cursor(api.search, tweet_mode='extended', q="#DisabilityInclusion",
                        lang="en",
                        since="2020-02-19").items()
    for tweet in get:  # items(5):
        msj = tweet.full_text
        msj = re.sub(r"http\S+", "", msj)
        msj = re.sub(r"@\S+", "", msj)
        # msj = re.sub(r"#\S+", "", msj)
        list.add(msj)
        # print (msj)
        # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

    #list.remove(        "RT  #Veterans with #disabilities face huge barriers when seeking #employment. Here's what  is doing to provide per…")
    # for x in list:
    #     print(x)
    #     count +=1
    # print(count)
    return list

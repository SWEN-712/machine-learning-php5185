import requests
# pprint is used to format the JSON response
from pprint import pprint
import os
import toJson

subscription_key = "8df7fd266c994b2d96cae75ecc5c1c6d"
endpoint = "https://eastus.api.cognitive.microsoft.com"
sentiment_url = endpoint + "/text/analytics/v2.1/sentiment/"
count =1;
# #format tweet to json here
# info = extractTweets.tweets()
#
# tweet = []
# for x in info:
#     id = str(count)
#     each ={
#         "id":id,
#         "text":x
#     }
#     count +=1
#     tweet.append(each)
#
# document = {
#     "documents": tweet
# }

documents = toJson.Json()

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)
import requests
# pprint is used to format the JSON response
from pprint import pprint
import os
import extractTweets
#
# subscription_key = "8df7fd266c994b2d96cae75ecc5c1c6d"
# endpoint = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.1/sentiment/"

count =1;
#format tweet to json here
info = extractTweets.tweets()

tweet = []
for x in info:
    id = str(count)
    each ={
        "id":id,
        "text":x
    }
    count +=1
    tweet.append(each)

document = {
    "documents": tweet
}

# headers = {"Ocp-Apim-Subscription-Key": subscription_key}
# response = requests.post(language_api_url, headers=headers, json=documents)
# languages = response.json()
# pprint(languages)
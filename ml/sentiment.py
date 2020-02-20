import requests
# pprint is used to format the JSON response
from pprint import pprint
import os
import toJson

subscription_key = "8df7fd266c994b2d96cae75ecc5c1c6d"
endpoint = "https://eastus.api.cognitive.microsoft.com"
sentiment_url = endpoint + "/text/analytics/v2.1/sentiment/"
count =1;

documents = toJson.Json()

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_url, headers=headers, json=documents)
sentiments = response.json()

if "documents" in sentiments:
    list = sentiments["documents"]

    sum =0
    size = 0
    max =0
    text = ""
    id = ""
    for item in list:
        pts = item["score"]
        sum +=pts
        size +=1
        if pts>max:
            max=pts
            id = item["id"]

    if "documents" in documents:
        findTweet = documents["documents"]
        for t in findTweet:
            if t["id"] == id:
                text = t["text"]
                break
            #text = item["text"]

    avr = sum/size

    print("Average Sentiment Score: ", avr)
    if avr>=0.75:
        print("Positive sentiment on average")
    if avr<0.75 and avr>=0.50:
        print("Slightly positive sentiment on average")
    if avr<0.50 and avr>=0.25:
        print("Slightly negative sentiment on average")
    if avr<0.25:
        print("Negative sentiment on average")
    print()
    print("Most positive score:", max)
    print("Tweet text: ",text)
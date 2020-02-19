import extractTweets

def Json():
    count =0
    info = extractTweets.tweets()

    tweet = []
    for x in info:
        id = str(count)
        each ={
            "id":id,
            "language": "en",
            "text":x
        }
        count +=1
        tweet.append(each)

    document = {
        "documents": tweet
    }

    return document


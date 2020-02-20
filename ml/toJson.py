import extractTweets
import language
from pprint import pprint


def Json():
    count = 0
    # info = extractTweets.tweets()
    info = language.getTweets()
    tweet = []
    for x in info:
        id = str(count)
        each = {
            "id": id,
            "language": "en",
            "text": x
        }
        count += 1
        tweet.append(each)

    document = {
        "documents": tweet
    }

    #print(document)

    return document

if __name__ == "__main__":
    Json()
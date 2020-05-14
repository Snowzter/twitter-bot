import tweepy
import time

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN","ACCESS_TOKEN_SECRET")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'News'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        time.sleep(125)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# need o install tweepy, in console "pip install tweepy"
import tweepy
import time

auth = tweepy.OAuthHandler('API key','API Secret')
auth.set_access_token('Acess token','Access token secret')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'Keyword'
numero = 500000

for tweet in tweepy.Cursor(api.search, search).items(numero):
    try:
        print(tweet.text.encode("utf-8"))   
        print("username: @" + tweet.user.screen_name)
        api.update_status("@" + tweet.user.screen_name + " comment", in_reply_to_status_id=tweet.id)
        print("tweet sent correctly")
        tweet.favorite() #Command to like tweets
        print("Liked")
        print("///////")
        time.sleep(300)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
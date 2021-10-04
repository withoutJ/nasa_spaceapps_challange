import tweepy
from tweepy import OAuthHandler
import pandas as pd

access_token = 'put yout access token here'
access_token_secret = 'put your access token secret here'
consumer_key = 'put your consumer key here'
consumer_secret = 'put your consumer secret here'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_words = "(marine OR water OR river OR ocean OR coast OR beach OR river OR lake) (debris OR trash OR plastic OR junk OR plastic OR pollution OR garbage OR litter )" #keywords for search
count = 1
tweets = []

for tweet in tweepy.Cursor(api.search_tweets, q=search_words).items(100): #in items you can choose how many tweets you want to scrape, with twitter api there are limitations
	print(count)
	count += 1

	try:
		data = [tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name'], tweet.user._json['created_at'], tweet.entities['urls']]
		data = tuple(data)
		tweets.append(data)

	except tweepy.TweepError as e:
		print(e.reason)
		continue

	except StopIteration:
		break

df = pd.DataFrame(tweets, columns = ['created_at','tweet_id', 'tweet_text', 'screen_name', 'name', 'account_creation_date', 'urls'])

df.to_csv(path_or_buf = '/home/without_j/.venv/spaceapps/tweets.csv', index=False) #put your path to the file where you want to save tweets here

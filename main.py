from tweets_sentiment_analysis import senti_score
from finding_location import location

import pandas as pd

tweets = pd.read_csv('tweets.csv')

tweets_text = tweets['tweet_text']

locations = []

for text in tweets_text:
	if(senti_score(text)<0):
		locations.append(location(text))

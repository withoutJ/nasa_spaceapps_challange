import googlemaps

gmaps = googlemaps.Client(key='Add Your Key here')

def location(tweet_text):
	return gmaps.geocode(tweet_text)

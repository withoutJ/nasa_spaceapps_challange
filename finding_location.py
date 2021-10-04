import googlemaps

gmaps = googlemaps.Client(key='Add Your Key here')

def location(tweet_text):
	returun gmaps.geocode(tweet_text)

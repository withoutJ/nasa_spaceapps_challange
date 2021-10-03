import googlemaps

gmaps = googlemaps.Client(key='Add Your Key here')

def location(tweet_text):
	geocode_result = gmaps.geocode(tweet_text)

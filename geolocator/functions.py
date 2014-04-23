import urllib2
import json
from geopy.geocoders import GoogleV3

from apis import *

def find_place(query):
	g = GoogleV3()
	place, (lat, lng) = g.geocode(query)
	return place, lat, lng

def locu_search(query):
	api = locu_api
	url = "https://api.locu.com/v1_0/venue/search/?"

	local = query
	locality = local.replace(' ','%20')

	new_url = url + 'api_key=' + api + '&locality' + locality

	obj = urllib2.urlopen(new_url)
	data = json.load(obj)

	locations = []

	for abc in data['objects']:
		locations.append(abc['name'])

	return locations

def foursquare_search(query):
	token = foresquare_token

	place, lat, lng = find_place(query)
	latlng = str(lat) + "%2C" + str(lng)
	
	url = "https://api.foursquare.com/v2/venues/search?v=20131016&ll=" + latlng + "&intent=checkin&oauth_token="
	full_url = url + token

	obj = urllib2.urlopen(full_url)

	data = json.load(obj)

	locations = []

	for abc in data['response']['venues']:
		locations.append(abc['name'])
		
	return locations

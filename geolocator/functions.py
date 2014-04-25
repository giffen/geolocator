import urllib2
import json
from geopy.geocoders import GoogleV3

from apis import foresquare_token, locu_api

def find_city_lat_lng(lat, lng):
	g = GoogleV3()
	find = "%s %s" %(lat, lng)
	place, (lat, lng) = g.geocode(find)
	full_address = place.split(', ')
	city = full_address[1]
	return str(city)

def find_place(query):
	g = GoogleV3()
	place, (lat, lng) = g.geocode(query)
	return place, lat, lng


def locu_details(locu_id):
	api = locu_api
	url = "https://api.locu.com/v1_0/venue/"
	new_url = url + str(locu_id) + "/?api_key=" + api
	print new_url

	obj = urllib2.urlopen(new_url)
	data = json.load(obj)

	details = []

	for abc in data['objects']:
		details.append(abc['lat'])
		details.append(abc['long'])

	return details

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
		list_item = [abc['id'],abc['name']]
		locations.append(list_item)

	return locations


def foursquare_details(four_id):
	api = foresquare_token
	url = "https://api.foursquare.com/v2/venues/"
	new_url = url + str(four_id) + "?v=20131016&oauth_token=" + api
	print new_url

	obj = urllib2.urlopen(new_url)
	data = json.load(obj)

	details = []

	details.append(data['response']['venue']['location']['lat'])
	details.append(data['response']['venue']['location']['lng'])

	return details

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
		locations.append([abc['id'],abc['name']])
		
	return locations

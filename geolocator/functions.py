import urllib2
import json

from apis import *

api = locu_api
url = "https://api.locu.com/v1_0/venue/search/?"

def locu_search(query):
	local = query
	locality = local.replace(' ','%20')

	new_url = url + 'api_key=' + api + '&locality' + locality

	obj = urllib2.urlopen(new_url)
	data = json.load(obj)

	locations = []

	for abc in data['objects']:
		locations.append(abc['name'])

	return locations
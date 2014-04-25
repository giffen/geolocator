from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404

from locations.models import Location
from .functions import locu_search, foursquare_search, find_city_lat_lng

def home(request):
	if request.method == 'POST':
		q = request.POST['search']
		lat = request.POST['lat']
		lng = request.POST['lng']
		query = find_city_lat_lng(lat, lng)
		locations = locu_search(query)
		
		for loc in locations:
			locu_id, name = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name=name, locu_id=locu_id)
			if created:
				pass
				# print "Created new id for %s with id of %s" %(name, locu_id)
		
		'''
		locations = foursquare_search(q)
		for loc in locations:
			four_id, name = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name=name, four_id=four_id)
			if created:
				print "Created new id for %s with id of %s" %(name, four_id)
		'''
	return render_to_response('home.html', locals(), context_instance=RequestContext(request))
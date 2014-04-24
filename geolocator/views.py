from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404

from locations.models import Location
from .functions import locu_search, foursquare_search

def home(request):
	if request.method == 'POST':
		q = request.POST['search']
		locations = locu_search(q)
		for loc in locations:
			locu_id, name = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name=name, locu_id=locu_id)
			if created:
				print "Created new id for %s with id of %s" %(name, locu_id)

	return render_to_response('home.html', locals(), context_instance=RequestContext(request))
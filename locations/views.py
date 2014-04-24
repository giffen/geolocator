from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404

from geolocator.functions import locu_details
from .models import Location


def single_location(request, id):
	try:
		location = Location.objects.get(locu_id=id)
		locu = True
	except Location.DoesNotExist:
		location = Location.objects.get(four_id=id)
		foursquare = True
	except:
		location = "This Location cannot be found!"

	if locu:
		details = locu_details(location.locu_id)
	elif foursquare:
		details = False
	else:
		pass

	return render_to_response('locations/single.html', locals(), context_instance=RequestContext(request))

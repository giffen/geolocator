from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404

from .models import Location

def single_location(request, id):
	try:
		location = Location.objects.get(locu_id=id)
	except Location.DoesNotExist:
		location = Location.objects.get(four_id=id)
	except:
		location = "This Location cannot be found!"

	return render_to_response('locations/single.html', locals(), context_instance=RequestContext(request))

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404

from .functions import locu_search

def home(request):
	if request.method == 'POST':
		q = request.POST['search']
		locations = locu_search(q)
		print locations

	return render_to_response('home.html', locals(), context_instance=RequestContext(request))
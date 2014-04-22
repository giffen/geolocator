from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geolocator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^static/(?<path>.*)$, django.views.static.serve,{
    	'document_root': settings.STATIC_ROOT}),
    (r'^media/(?<path>.*)$, django.views.static.serve,{
    	'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)

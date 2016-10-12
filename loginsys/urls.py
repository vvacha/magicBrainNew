from django.conf.urls import include, url, patterns

from django.contrib import admin
from django.conf.urls import patterns, include, url, static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, urlpatterns
from django.conf import settings

#from django.conf import settings

urlpatterns = [
 
 url(r'^login/$', 'loginsys.views.login'),
 url(r'^logout/$', 'loginsys.views.logout'),
 url(r'^register/$', 'loginsys.views.register'),

]

urlpatterns += patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

# if settings.DEBUG:
# 	urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
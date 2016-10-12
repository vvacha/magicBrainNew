from django.conf.urls import url
from lesson import views
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls import patterns, include, url, static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, urlpatterns


urlpatterns = [
	url(r'^$', views.LessonListView.as_view(), name='lesson'),
	url(r'^(?P<lesson_id>\d+)/$', views.lesson),

]

urlpatterns += patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myFakingSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls')),
    url(r'^lessons/', include('lesson.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^userpage/', include('userpage.urls')),
) #+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += patterns('',
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

# urlpatterns += patterns('',
#   (r'^myFakingSite/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT }),
#  )

    #url(r'^polls/', include('polls.urls', namespace="polls")),
    #url(r'^chyvak/', include('article.urls')),
#from django.conf.urls import include, url, patterns
#from django.contrib import admin

#from django.conf import settings

#urlpatterns = [
 #   url(r'^', include('home.urls')),
 #   url(r'^admin/', include(admin.site.urls)),
 #   url(r'^vvacha/', include('post.urls')),
#	url(r'^polls/', include('polls.urls', namespace="polls")),
  #  url(rw'^lessons/', include('lessons.urls')),

  #  url(r'^basicview/', include('article.urls')),
   # url(r'^chyvak/', include('article.urls')),


    
#]


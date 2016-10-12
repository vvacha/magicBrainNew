from django.conf.urls import url
from lesson import views
from userpage import views
from userpage.controller import upload_image_tmp

urlpatterns = [
	url(r'^$', views.UserDataView.as_view(), name='userpage'),
	url(r'edit-profile/(?P<pk>\d+)/$', views.UserUpdate.as_view(), name='user_update'),
	url(r'user/image/tmp/$', upload_image_tmp),
	
]

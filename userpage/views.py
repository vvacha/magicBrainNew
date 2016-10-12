# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views import generic
from django.contrib import auth
from .forms import SettingForm
from django.core.context_processors import csrf
from userpage.models import CustomUser
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect

# Create your views here.

class UserDataView(generic.TemplateView):
	template_name = 'userpage/userpage.html'

	def get_context_data(self, **kwargs):
		context = super(UserDataView, self).get_context_data(**kwargs)
		context['username'] = auth.get_user(self.request).username
		context['userdata'] = auth.get_user(self.request)
		return context	


class UserUpdate(UpdateView):
	form_class = SettingForm
	model = CustomUser
	template_name = 'userpage/usersetting.html'
	success_url = '/userpage/'

	def get(self, request, **kwargs):
		return super(UserUpdate, self).get(request, **kwargs)

	def post(self, request, **kwargs):
		avatar = request.POST.get('input-avatar-url', '')
		city = request.POST.get('city', '')
		user = self.get_object()
		if avatar:
			user.avatar = avatar
		else:	 
			user.avatar = user.avatar
		user.city = city
		user.save()
		return super(UserUpdate, self).post(request, **kwargs)
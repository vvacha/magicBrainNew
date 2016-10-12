from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import NameForm, ContactForm


# Create your views here.

class HomeView(generic.TemplateView):
	template_name = 'home/home.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['username'] = auth.get_user(self.request).username
		return context	


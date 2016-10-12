from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from .forms import UserCreationForm

def login(request):

	print("ghfhfghkgfhfh!!!!--hello-->>>>>", request)
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		print("!!!uSER naame!!!", username)
		password = request.POST.get('password', '')
		print("!!!password naame!!!", password)
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error']="Пользователь не найден"
			return render_to_response('home/home.html', args)
	else:
		return render_to_response('home/home.html', args)

def logout(request):
	auth.logout(request)
	return redirect('/')


def register(request):
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		error = newuser_form.errors.as_data()   
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
			auth.login(request, newuser)
			return redirect('/')
		else:
			error = newuser_form.errors   
			args['form'] = newuser_form

	return render_to_response('loginsys/register.html', args)


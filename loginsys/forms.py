# -*- coding: utf-8 -*-
from django import forms
# from .models import Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from userpage.models import CustomUser


class MultiEmailField(forms.Field):
	
	def to_python(self, value):
		"Normalize data to a list of strings."
		# Return an empty list if no input was given.
		if not value:
			return []

		v = value.split(',')
		return value.split(',')

	def validate(self, value):
		"Check if value consists only of valid emails."

		# Use the parent's handling of required fields, etc.
		super(MultiEmailField, self).validate(value)

		for email in value:
			validate_email(email)

class UserCreationForm(UserCreationForm):						
	"""docstring for UserCreateForm"""
	recipients = MultiEmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Fifst name'}))
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last name'}))
	username = forms.CharField()
	password1 = forms.CharField()
	password2 = forms.CharField()

	def clean_recipients(self):
		data = self.cleaned_data['recipients']
		if User.objects.filter(email=data[0]).exists():
			raise forms.ValidationError("Этот E-mail используется")
		return data
		
	class Meta:
		fields = ['recipients', 'username', 'first_name', 'last_name', 'password1', 'password2']	
		model = CustomUser























	# def is_valid(self):
	# 	print('!!!!!!ZIGA+ZAGA!!!!!!')
	# 	form = super(UserCreationForm, self).is_valid()
		

	# 	d = self.errors
	# 	print('!!!!!!ZIGA!!!!!!', d)
	# 	for f, error in self.errors.iteritems():
	# 		if f != '__all_':
	# 			self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
	# 	return form


		# mail=data[0]
		# mailInDB = User.objects.filter(email=mail)
		# if User.objects.filter(email_iexact=mail).exists(): 
		# 	raise forms.ValidationError()




# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         fields = ['comments_text']
#         #exclude = ()




		# print('____prishlo v data___----->', data)
		# spisok_mailov = User.objects.values('email')

				# args['error'] = "ЛОГИН ЗАНЯТ"
		# v = str(spisok2)
		# her = 'her her her her her her her her her'
		# print('____SPISOK2___----->', spisok2, type(spisok2), "------------------", her, type(her))
		# print('________V_______', v, type(v))
		# print("--------vVOT TYT-------/....>>>", spisok_mailov, "||||||||", type(spisok_mailov))
		# for mail in spisok_mailov:
			# a=data[0]
			# print("__________A______", a, type(a))
			# b=str(mail)
			# print("__________B______", a, type(b))
			# print('------mail------>>>', mail, data, "|||||||", type(mail), "|||||||", type(data))
#				return render_to_response('home/main.html', args)
		# if "fred@example.com" not in data:
		# 	raise forms.ValidationError("этот емаил зарегестрирован")
	




	# email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
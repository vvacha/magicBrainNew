from django import forms
from django.core.validators import validate_email

class MultiEmailField(forms.Field):
	def to_python(self, value):
		"Normalize data to a list of strings."

		# Return an empty list if no input was given.
		if not value:
			return []
		return value.split(',')

	def validate(self, value):
		"Check if value consists only of valid emails."

		# Use the parent's handling of required fields, etc.
		super(MultiEmailField, self).validate(value)

		for email in value:
			validate_email(email)

class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()
	recipients = MultiEmailField()
	cc_myself = forms.BooleanField(required=False)


	def clean_recipients(self):
		data = self.cleaned_data['recipients']
		print('____prishlo v data___----->', data)
		if "fred@example.com" not in data:
			raise forms.ValidationError("этот емаил зарегестрирован")

		# Always return the cleaned data, whether you have changed it or not.
		return data

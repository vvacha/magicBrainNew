from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.

class CustomUser(User):
	"""User with app settings."""
	city = models.CharField(max_length=50, null=True, blank=True, default = 'No_city')
	avatar = models.ImageField(null=True, blank=True, upload_to="avatar/", default = '/media/NoAvatar/No_avatar.jpg')
	# Use UserManager to get the create_user method, etc.
	objects = UserManager()

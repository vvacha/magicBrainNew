from django.db import models

# Create your models here.

class Lesson(models.Model):
	class Meta():
		db_table = "lesson"

	def __str__(self):  # __unicode__ on Python 2
		return self.lesson_name
	lesson_name = models.CharField(max_length = 200)
	lesson_text = models.TextField()
	lesson_creator = models.CharField(max_length = 200)
	lesson_image = models.ImageField(null=True, blank=True, upload_to="images/" )
	#avatar_lesson = models.ImageField(upload_to = "C:")
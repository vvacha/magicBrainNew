from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Lesson
from django.core.context_processors import csrf
from django.contrib import auth
from MagicBrain import settings

# Create your views here.

class LessonListView(generic.ListView):
	template_name = 'lessons/lessonsList.html'
	context_object_name = 'lesson_lists'

	def get_context_data(self, **kwargs):
		context = super(LessonListView, self).get_context_data(**kwargs)
		context['username'] = auth.get_user(self.request).username
		return context	

	def get_queryset(self):
		return Lesson.objects.all()

def lesson(request, lesson_id=1):
	args= {}
	args.update(csrf(request))
	args['lesson'] = Lesson.objects.get(id=lesson_id)
	args['username'] = auth.get_user(request).username
	return render(request, 'lessons/lesson.html', args)	

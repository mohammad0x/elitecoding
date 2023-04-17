from django.shortcuts import render
from .models import *


def Home(request):
    post = Post.objects.filter(status='p').order_by('-publish')
    context = {'posts': post}
    return render(request, 'administrator/Home/home.html', context)


def course_View(request):
    course = Course.objects.all().order_by('-publish')
    context = {
        'course': course
    }
    return render(request, 'administrator/course/course.html', context)

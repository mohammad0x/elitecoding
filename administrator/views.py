from django.shortcuts import render, get_object_or_404
from .models import *


def Home(request):
    post = Post.objects.filter(status='p').order_by('-publish')
    context = {'posts': post}
    return render(request, 'administrator/Home/home.html', context)


def detail_Post(request, slug):
    detail = get_object_or_404(Post, slug=slug , status='p')
    context = {
        'detail':detail
    }
    return render(request , 'administrator/Home/detail.html' , context)


def course_View(request):
    course = Course.objects.all().order_by('-publish')
    context = {
        'course': course
    }
    return render(request, 'administrator/course/course.html', context)

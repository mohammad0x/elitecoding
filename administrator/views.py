from django.shortcuts import render
from .models import *


# Create your views here.
def post_Views(request):
    post = Post.objects.filter(status='p').order_by('-publish')
    context = {'posts':post}
    return render(request , 'shop/Home/home.html' , context)


def course_View(request):
    course = Course.objects.all().order_by('-publish')
    context = {
        'course':course
    }
    return render (request , '' , context)
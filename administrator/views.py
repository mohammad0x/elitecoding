from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from shop.models import MyUser


def Home(request):
    post = Post.objects.filter(status='p').order_by('-publish')
    context = {'posts': post}
    return render(request, 'administrator/Home/home.html', context)


def detail_Post(request, slug):
    detail = get_object_or_404(Post, slug=slug, status='p')
    context = {
        'detail': detail
    }
    return render(request, 'administrator/Home/detail.html', context)


def course_View(request):
    course = Course.objects.all().order_by('-publish')
    context = {
        'course': course
    }
    return render(request, 'administrator/course/course.html', context)


def video_Course(request, id):
    video = Video.objects.filter(course_id=id)
    context = {
        'video': video
    }
    return render(request, 'administrator/video/video.html', context)


def cart(request , id):
    user = request.user.id
    course = id
    carts = Cart.objects.create(user_id=user , course_id=course)
    carts.save()
    return HttpResponse("ok")


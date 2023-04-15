from django.shortcuts import render
from .models import Post


# Create your views here.
def post_Views(request):
    post = Post.objects.filter(status='p').order_by('-publish')
    context = {'posts':post}
    return render(request , 'administrator/index/index.html' , context)
from django.urls import path
from .views import *

urlpatterns = [
    path('post/' , post_Views , name= 'post'),
    path('course/' , course_View , name= 'course'),
]
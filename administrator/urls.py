from django.urls import path
from .views import *
app_name='administrator'
urlpatterns = [
    path('home/', Home, name="home"),
    path('detail/<slug:slug>/', detail_Post, name="detail_Post"),
    path('course/' , course_View , name= 'course'),
]
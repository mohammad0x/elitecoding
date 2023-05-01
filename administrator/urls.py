from django.urls import path
from .views import *
app_name='administrator'
urlpatterns = [
    path('home/', Home, name="home"),
    path('detail/<slug:slug>/', detail_Post, name="detail_Post"),
    path('video_Course/<int:id>/', video_Course, name="video_Course"),
    path('course/' , course_View , name= 'course'),
    path('cart/<int:id>' , cart , name= 'cart'),
    path('myCourse/<int:id>/' , myCourse , name= 'myCourse'),
]
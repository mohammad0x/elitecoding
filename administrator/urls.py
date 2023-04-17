from django.urls import path
from .views import *
app_name='administrator'
urlpatterns = [
    path('home/', Home, name="home"),
    path('course/' , course_View , name= 'course'),
]
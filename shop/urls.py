from django.urls import path
from .views import *
urlpatterns = [
    path('home/', Home, name="home"),
    path('login/' , Login , name="login"),
    path('register/' , Register , name="register"),
]

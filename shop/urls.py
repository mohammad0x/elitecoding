from django.urls import path
from .views import *
app_name = 'shop'
urlpatterns = [
    path('home/', Home, name="home"),
    path('login/' , Login , name="login"),
    path('register/' , Register , name="register"),
    path('profile/' , ProfileUpdate , name="profileUpdate"),
    path('profileView/' , profile_view , name="profile_view"),
    path('logout/' , Logout_view , name="logout"),
]

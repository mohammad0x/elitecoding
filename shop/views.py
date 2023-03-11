from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            context = {
                "username": username,
                "errormessage": "User not found"
            }
            return render(request, "shop/login/login.html", context)
    else:
        return render(request, 'shop/login/login.html', {})

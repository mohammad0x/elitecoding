from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *


# Create your views here.


def Home(request):
    return render(request, 'shop/Home/home.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:home')
        else:
            context = {
                "username": username,
                "errormessage": "User not found"
            }
            return render(request, "shop/Login/login.html", context)
    else:
        return render(request, 'shop/Login/login.html', {})


def Register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(email=data['email'], username=data['username'], password=data['password'])
            user.save()
            return redirect('shop:login')
        else:
            messages.error(request, 'Something is wrong! Please try again', 'danger')
    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'shop/Register/register.html', context)


def Logout_view(request):
    logout(request)
    return redirect('shop:login')


def ProfileUpdate(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profiles)
        if profile_form.is_valid() or user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Update Successfully', 'success')
            return redirect('shop:home')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profiles)
    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'shop/profile/UpdateProfile.html', context)

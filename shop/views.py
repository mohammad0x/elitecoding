from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from kavenegar import *
import random


# Create your views here.




def Login(request):
    if request.user.is_authenticated:
        return redirect('administrator:home')
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('administrator:home')
        else:
            context = {
                "username": username,
                "errormessage": "User not found"
            }
            return render(request, "shop/Login/login.html", context)
    else:
        return render(request, 'shop/Login/login.html', {})


def Register(request):
    if request.user.is_authenticated:
        return redirect('blog:profile')
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


@login_required(login_url='/login/')
def profile_view(request):
    profile = Profile.objects.filter(user_id=request.user.id)
    context = {
        'profile': profile
    }
    return render(request, 'shop/profile/Profile.html', context)


@login_required(login_url='/login/')
def ProfileUpdate(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profiles)
        if profile_form.is_valid() or user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Update Successfully', 'success')
            return redirect('administrator:home')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profiles)
    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'shop/profile/UpdateProfile.html', context)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'shop/passwordReset/password_reset.html'
    email_template_name = 'shop/passwordReset/password_reset_email.html'
    subject_template_name = 'shop/passwordReset/password_reset_subjects'
    success_message = "اگر ثبت نام نکرده اید لطفا ثبت نام کنبد"

    success_url = reverse_lazy('shop:register')


def login_phone(request):
    if request.method == 'POST':
        form = LoginPhoneForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            global phone, random_code
            phone = f"{data['phone']}"
            random_code = random.randint(1000, 9999)
            sms = KavenegarAPI(
                "********")
            params = {
                'sender': '******',  # Array of String
                'receptor': '*****',  # Array of String
                'message': f' {random_code} سلام این اولین تست است ',
            }
            response = sms.sms_send(params)
            return redirect('shop:verify_login_phone')
    else:
        form = LoginPhoneForm()
    context = {
        'form': form,
    }
    return render(request, 'shop/phone/login-phone.html', context)


def verify_login_phone(request):
    if request.method == 'POST':
        form = CodePhoneForm(request.POST)
        if form.is_valid():
            if str(random_code) == form.cleaned_data['verify_code']:
                profile = Profile.objects.filter(user_id=request.user.id).update(phone=phone)
                return redirect('shop:login')
            else:
                print("4")
                messages.error(request, 'کد وارد شده اشتباه است')
    else:
        form = CodePhoneForm()
    context = {
        'form': form,
    }
    return render(request, 'shop/phone/verify-login-phone.html', context)

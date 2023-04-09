from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'shop'
urlpatterns = [
    path('home/', Home, name="home"),
    path('login/' , Login , name="login"),
    path('register/' , Register , name="register"),
    path('profile/' , ProfileUpdate , name="profileUpdate"),
    path('profileView/' , profile_view , name="profile_view"),
    path('logout/' , Logout_view , name="logout"),
    path('login_phone/' , login_phone , name="login_phone"),
    path('verify_login_phone/' , verify_login_phone , name="verify_login_phone"),
    # Forget password
    path('password-reset/', ResetPasswordView.as_view(success_url=reverse_lazy('shop:password_reset_done')),
         name='password_reset'),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name="shop/passwordReset/password_reset_done.html"),
         name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('hair_style:password_reset_complete'),
                                                     template_name='shop/passwordReset/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='shop/passwordReset/password_reset_complete.html'),
         name='password_reset_complete'),
]


from django import forms
from .models import *


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_Confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email', 'username']

    def clean_password2(self):
        data = self.cleaned_data
        if data['password_Confirmation'] and data['password'] and data['password_Confirmation'] != data['password']:
            raise forms.ValidationError('Passwords are not the same')
        return data['password_Confirmation']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password_Confirmation'])
        if commit:
            user.save()
        return user

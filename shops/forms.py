from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your UserName"}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your Email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter your password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter confirm password"}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
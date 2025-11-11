from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Item

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu usuario',
            'class': 'form-control'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'password',
            'class' : 'form-control'
        }
    ))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

        username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu usuario',
            'class': 'form-control'
        }
    ))
        email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Tu email',
            'class': 'form-control'
        }
    ))
        password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'password',
            'class' : 'form-control'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Repiet password',
            'class' : 'form-control'
        }
    ))

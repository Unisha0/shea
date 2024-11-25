# shea/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password1', 'password2']

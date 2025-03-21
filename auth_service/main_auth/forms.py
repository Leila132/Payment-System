from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'phone', 'first_name', 'last_name', 'country')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
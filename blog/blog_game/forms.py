from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', max_length=100,
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='Электронная почта',
                             widget=forms.EmailInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', max_length=100,
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-control"}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(label='Ваша почта', widget=forms.EmailInput(attrs={'class': "form-control"}))
    subject = forms.CharField(label='Тема', max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': "form-control"}))

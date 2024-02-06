from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        password = self.cleaned_data['password1']
        again_password = self.cleaned_data['password2']

        if password != again_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth
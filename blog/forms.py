from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=100,widget=forms.TextInput({
        'class':'form-control',
        'placeholder':'用户名',
    }))
    pwd=forms.CharField(max_length=20,widget=forms.PasswordInput({
        'class':'form-control',
        'placeholder':'密码',
    }))
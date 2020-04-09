from django import forms
from django.contrib.auth.forms import AuthenticationForm
from ckeditor.fields import RichTextField
from .models import Category
from django.utils.translation import ugettext_lazy as _

class LoginForm(AuthenticationForm):
    LoUsername=forms.CharField(max_length=12,widget=forms.TextInput({
        'class':'form-control',
        'placeholder':'用户名',
    }))
    LoPwd=forms.CharField(max_length=20,widget=forms.PasswordInput({
        'class':'form-control',
        'placeholder':'密码',
    }))
class ArticleForm(forms.Form):
    title=forms.CharField(label='title',max_length=150,widget=forms.TextInput({
        'class':'form-control',
        'placeholder':'标题',
    }))
    cover=forms.ImageField(allow_empty_file=True)
    body=forms.CharField()
class RegisterForm(forms.Form):
    ReUsername=forms.CharField(label='用户名',max_length=12,widget=forms.TextInput({
        'class':'form-control',
        'placeholder':'用户名',
    }))
    RePwd=forms.CharField(label='密码',max_length=20,widget=forms.PasswordInput({
        'class':'form-control',
        'placeholder':'密码',
    }))
    RePwd2=forms.CharField(label='再次输入密码',max_length=20,widget=forms.PasswordInput({
        'class':'form-control',
        'placeholder':'再次输入密码',
    }))
    ReEmail=forms.EmailField(label='email',widget=forms.EmailInput({
        'class':'form-control',
        'placeholder':'邮箱地址',
    }))
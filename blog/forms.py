from django import forms
from django.contrib.auth.forms import AuthenticationForm
from ckeditor.fields import RichTextField
from .models import Category
from django.utils.translation import ugettext_lazy as _

class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=100,widget=forms.TextInput({
        'class':'form-control',
        'placeholder':'用户名',
    }))
    pwd=forms.CharField(max_length=20,widget=forms.PasswordInput({
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

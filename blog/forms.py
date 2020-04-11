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
    title=forms.CharField(max_length=150,widget=forms.TextInput({
        'class':'form-control',
        'placeholder':'标题',
    }))
    cover=forms.URLField(widget=forms.TextInput({
        'class':'form-control',
        'placeholder':'封面图片地址'
    }))
    category=forms.ChoiceField(choices=Category.objects.values_list('category','category'))
    # category=forms.ModelChoiceField(label=u'分类',queryset=Category.objects.all(),empty_label=None)
class RegisterForm(forms.Form):
    ReUsername=forms.CharField(max_length=12,widget=forms.TextInput({
        'class':'form-control',
        'placeholder':'用户名',
    }))
    RePwd=forms.CharField(max_length=20,widget=forms.PasswordInput({
        'class':'form-control',
        'placeholder':'密码',
    }))
    RePwd2=forms.CharField(max_length=20,widget=forms.PasswordInput({
        'class':'form-control',
        'placeholder':'再次输入密码',
    }))
    ReEmail=forms.EmailField(widget=forms.EmailInput({
        'class':'form-control',
        'placeholder':'邮箱地址',
    }))
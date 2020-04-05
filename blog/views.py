from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from .models import Category
from .forms import LoginForm

# Create your views here.

def index(request):
    AllCategory = Category.objects.all()
    context = {
        'form':LoginForm,
        'AllCategory': AllCategory,
    }
    if request.method=='GET':
        return render(request, 'blog/index.html', context)
    elif request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        user=auth.authenticate(username=username,password=pwd)
        if user:
            auth.login(request,user)
        else:
            return render(request, 'blog/index.html', context)

def category(request, category_id):
    return HttpResponse("这是分类页面%s" % category_id)

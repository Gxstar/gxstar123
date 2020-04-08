from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from .models import Category,Article
from .forms import LoginForm,ArticleForm,RegisterForm
from django.contrib.auth.models import User
# Create your views here.
# 首页逻辑
def index(request):
    AllCategory = Category.objects.all()
    ListArticle=Article.objects.order_by('-id')[0:3]
    context = {
        'LoginForm':LoginForm,
        'AllCategory': AllCategory,
        'errorMsg':'',
        'ListArticle':ListArticle,
        'currentuser':request.user,
    }
    if request.method=='GET':
        return render(request, 'blog/index.html', context)
    elif request.method=='POST': 
        username=request.POST.get('LoUsername')
        pwd=request.POST.get('LoPwd')
        if 'login' in request.POST:
            user=auth.authenticate(username=username,password=pwd)
            if user:
                auth.login(request,user)
            else:
                context.update(errorMsg='请输入正确的用户名密码！')
                return render(request, 'blog/index.html', context)
        else:
            ReContext=context
            ReContext['ReForm']=RegisterForm
            ReContext['ReUsername']=username
            ReContext['RePwd']=pwd
            return render(request, 'blog/register.html', ReContext)
    return render(request, 'blog/index.html', context)
def category(request, category_id):
    return HttpResponse("这是分类页面%s" % category_id)
# 文章编辑页面
def article_edit(request,article_id):
    article=Article.objects.get(id=article_id)
    myform=ArticleForm()
    context={
        'article':article,
        'myform':myform,
    }
    return render(request,'blog/article_edit.html',context)
# 注册页面
def regist(request):
    username=request.POST.get('ReUsername')
    email=request.POST.get('ReEmail')
    pwd=request.POST.get('RePwd')
    
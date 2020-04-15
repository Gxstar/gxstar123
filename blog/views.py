from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from .models import Category,Article
from .forms import LoginForm,ArticleForm,RegisterForm
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
# Create your views here.
# 首页逻辑
def index(request):
    AllCategory = Category.objects.all()
    ListArticle=Article.objects.order_by('-id')[0:3]
    for index,val in enumerate(ListArticle):
        bs=BeautifulSoup(val.body,"lxml")
        i=bs.text[0:30]
        ListArticle[index].info=i
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
                return render(request, 'blog/index.html', context)
            else:
                context.update(errorMsg='请输入正确的用户名密码！')
                return render(request, 'blog/index.html', context)
        else:
            ReContext=context
            ReContext['ReForm']=RegisterForm
            ReContext['ReUsername']=username
            ReContext['RePwd']=pwd
            return render(request, 'blog/register.html', ReContext)
def category(request, category_id):
    return HttpResponse("这是分类页面%s" % category_id)
# 文章编辑页面
def article_edit(request,article_id):
    article=Article.objects.get(id=article_id)
    AllCategory = Category.objects.all()
    myform=ArticleForm
    context={
        'LoginForm':LoginForm,
        'AllCategory': AllCategory,
        'errorMsg':'',
        'currentuser':request.user,
        'article':article,
        'myform':myform,
    }
    return render(request,'blog/article_edit.html',context)
# 文章展示页面
def showArticle(request,article_id):
    AllCategory = Category.objects.all()
    article=Article.objects.get(id=article_id)
    context = {
        'LoginForm':LoginForm,
        'AllCategory': AllCategory,
        'errorMsg':'',
        'currentuser':request.user,
        'article':article
    }
    return render(request,'blog/article_show.html',context)
# 分类展示页面
def showCategory(request,category_id):
    ListArticle=Article.objects.filter(category__id=category_id).order_by('-id')[0:3]
    AllCategory = Category.objects.all()
    for index,val in enumerate(ListArticle):
        bs=BeautifulSoup(val.body,"lxml")
        i=bs.text[0:30]
        ListArticle[index].info=i
    context = {
        'LoginForm':LoginForm,
        'AllCategory': AllCategory,
        'errorMsg':'',
        'ListArticle':ListArticle,
        'currentuser':request.user,
    }
    return render(request,'blog/index.html',context)
# 保存文章
def saveArticle(request):
    articleid=request.POST.get('id')
    title=request.POST.get('title')
    author=request.POST.get('author')
    cover=request.POST.get('cover')
    body=request.POST.get('body')
    category=request.POST.get('category')
    article=Article.objects.get(id=articleid)
    article.title=title
    article.author=User.objects.get(username=author)
    article.cover=cover
    article.body=body
    article.category=Category.objects.get(category=category)
    article.save()
    return HttpResponse("文章保存成功！")
# 注册页面
def regist(request):
    username=request.POST.get('ReUsername')
    email=request.POST.get('ReEmail')
    pwd=request.POST.get('RePwd')
    pwd2=request.POST.get('RePwd2')
    checkUser=User.objects.filter(username=username)
    if pwd!=pwd2:
        return HttpResponse('两次密码输入不一致请重新输入')
    elif checkUser:
        return HttpResponse('用户名已存在')
    else:
        User.objects.create_user(username,email,pwd)
        user=auth.authenticate(username=username,password=pwd)
        auth.login(request,user)
        return redirect('/blog/')
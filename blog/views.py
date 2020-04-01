from django.shortcuts import render,HttpResponse
from .models import Category
# Create your views here.
def index(request):
    AllCategory=Category.objects.all()
    context={
        'AllCategory':AllCategory,
    }
    return  render(request,'blog/index.html',context)
def category(request,category_id):
    return HttpResponse("这是分类页面%s" % category_id)
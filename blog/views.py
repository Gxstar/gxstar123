from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request,'blog/index.html',{'title':'这是参数标题'})
from django.shortcuts import render
from .models import Category
# Create your views here.
def index(request):
    AllCategory=Category.objects.all()
    context={
        'AllCategory':AllCategory,
    }
    return  render(request,'blog/index.html',context)
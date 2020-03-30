from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    # 返回今日bing图片
    url="https://cn.bing.com/HPImageArchive.aspx?idx=0&n=1"
    data=requests.get(url).text
    soup=BeautifulSoup(data,'xml')
    src="https://cn.bing.com"+soup.find('url').contents[0]
    return redirect(src)
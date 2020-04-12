from django.urls import path,include,re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from . import forms

urlpatterns = [
    path('', views.index,name='bloghome'),
    path('category_<int:category_id>/',views.category,name='category'),
    re_path(r'^(.*)logout/$',LogoutView.as_view(next_page='/blog/'), name='logout'),
    path('article_edit_<int:article_id>',views.article_edit,name='article_edit'),
    path('regist/',views.regist,name='regist'),
    path('saveArticle/',views.saveArticle,name="saveArticle")
]

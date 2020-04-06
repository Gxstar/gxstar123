from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from . import forms

urlpatterns = [
    path('', views.index,name='home'),
    path('category_<int:category_id>/',views.category,name='category'),
    path('logout/',LogoutView.as_view(next_page='/blog/'), name='logout'),
    path('article_edit/<int:article_id>',views.article_edit,name='article_edit')
]

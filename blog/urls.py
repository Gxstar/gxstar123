from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from . import forms

urlpatterns = [
    path('', views.index,name='home'),
    path('category_<int:category_id>/',views.category,name='category'),
    path('log/',
         LoginView.as_view
         (
             template_name='blog/log.html',
             authentication_form=forms.LoginForm,
         ),
         name='log'),
    path('logout/',LogoutView.as_view(next_page='/blog/'), name='logout'),
]

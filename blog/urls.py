from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index,name='home'),
    path('category_<int:category_id>/',views.category,name='category'),
    path('login/',
         LoginView.as_view
         (
             template_name='blog/login.html',
             extra_context=
             {
                 'title': 'Log in',
             }
         ),
         name='login'),
    path('logout/',LogoutView.as_view(next_page='blog/'), name='logout'),
]

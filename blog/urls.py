from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('category_<int:category_id>/',views.category,name='category')
]

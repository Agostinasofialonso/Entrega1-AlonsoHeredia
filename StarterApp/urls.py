
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from StarterApp import views
from django.views.generic import TemplateView 

app_name= "StarterApp"

urlpatterns = [
    path('', views.StarterApp, name='StarterApp'),
    path('cats/create/', views.createcats, name='createcats'),
    path('dogs/create/', views.createdogs, name='createdogs'),
    path('birds/create/', views.createbirds, name='createbirds'),
    path('search/', views.search, name='search'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]


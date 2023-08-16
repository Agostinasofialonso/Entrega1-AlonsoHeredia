from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView 

app_name= "StarterApp"

urlpatterns = [
    path('', views.StarterApp, name='StarterApp'),
    path("aboutus/", views.aboutus, name = 'aboutus'),
    path('cats/create/', views.createcats, name='createcats'),
    path('dogs/create/', views.createdogs, name='createdogs'),
    path('birds/create/', views.createbirds, name='createbirds'),
    path('search/', views.search, name='search'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', TemplateView.as_view(template_name='start/start.html'), name='start'),
    path('delete/cat/<int:pk>/', views.deletecat, name='deletecat'),
    path('delete/dog/<int:pk>/', views.deletedog, name='deletedog'),
    path('delete/bird/<int:pk>/', views.deletebird, name='deletebird'),
    path('edit/cat/<int:pk>/', views.editcat, name='editcat'),
    path('edit/dog/<int:pk>/', views.editdog, name='editdog'),
    path('edit/bird/<int:pk>/', views.editbird, name='editbird'),
]



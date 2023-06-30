
from django.urls import path
from StarterApp import views

app_name= "StarterApp"

urlpatterns = [
    path('', views.StarterApp, name='StarterApp'),
    path('cats/create/', views.createcats, name='createcats'),
]


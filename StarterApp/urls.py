from django.urls import path
from StarterApp import views
urlpatterns=[
    path ('', views.start, name='Start')
]
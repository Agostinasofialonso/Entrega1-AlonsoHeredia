from django.urls import path
from user_app import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", views.iniciar_sesion, name='login'),
    path("logout/", LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path("profile/", views.verPerfil, name='profile'),
    path("profile/edit/", views.editar_perfil, name='editprofile'),
    path("password/edit/", views.editpassword.as_view(), name='editpassword'),
     path('profile/', views.verPerfilView.as_view(), name='profile'),
]
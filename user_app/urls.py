from django.urls import path
from Usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.registrarse, name = 'register'),
    path("login/", views.ingresar, name = 'login'),
    path("logout/", LogoutView.as_view(template_name='login/logout.html'), name = 'logout'),
    path("profile/", views.verPerfil , name = 'profile'),
    path("profile/edit/", views.editar_perfil , name = 'editprofile'),
    path("password/edit/", views.CambiarPassword.as_view(), name = 'editpassword'),
]
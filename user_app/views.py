from django.shortcuts import render, redirect
from user.forms import register, editprofile, editpasswordForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from Usuarios.models import InfoExtra
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import views
from django.contrib.auth.models import user

def register(request):
    if request.method == 'POST':
        formulario = CrearUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
        else:
            return render(request, 'Register/register.html', {'form': formulario})
    
    formulario = CrearUsuario()
    return render(request, 'Register/register.html', {'form': formulario})

def login (request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            user = authenticate(username=usuario, password=contraseña)
            
            login(request, user)
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('start')
        else:
            return render(request, 'Login/login.html', {'form': formulario})
        
    formulario = AuthenticationForm()
    return render(request, 'Login/login.html', {'form': formulario})

@login_required
def verPerfil(request):
    return render(request, 'Register/profile.html')

@login_required
def editar_perfil(request): 
    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            fechaNacimiento = formulario.cleaned_data.get('fechaNacimiento')
            if fechaNacimiento:
                info_extra_user.fechaNacimiento = fechaNacimiento
                info_extra_user.save()
            
            formulario.save()
            return redirect('profile')
    
    return render(request, 'Register/editprofile.html', {'form': formulario})

class editpassword(LoginRequiredMixin, View):
    template_name = 'Register/editpassword.html'
    form_class = CambiarPasswordForm
    success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.filter(id=request.user.id)
            if user.exists():
                user = user.first()
                user.set_password(form.cleaned_data.get('password1'))
                user.save()
                return redirect(self.success_url)
            return redirect(self.success_url)
        else:
            form = self.form_class(request.POST)
            return render(request, self.template_name, {'form': form})
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cats, Dogs, Birds
from .forms import CreateCatsForm, CreateDogsForm, CreateBirdsForm
from django.utils.translation import gettext as _

def some_view(request):
    translated_text = _('Texto a traducir')
# Create your views here.

def StarterApp (request):
    return render(request, 'start/start.html')
    
def createcats(request):
    mensaje = "Aquí puedes crear un gato"

    if request.method == "POST":
        formulario = CreateCatsForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            gato = Cats(nombre=info["nombre"], edad=info["edad"], fecha_nacimiento=info["fecha_nacimiento"])
            gato.save()
            mensaje = f"Se creó el gato {gato.nombre}"
        else:
            return render(request, "start/createcats.html", {"formulario": formulario})

    formulario = CreateCatsForm()
    return render(request, "start/createcats.html", {"formulario": formulario, "mensaje": mensaje})

def createdogs(request):
    mensaje = "Aquí puedes crear un perro"

    if request.method == "POST":
        formulario = CreateDogsForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            perro = Dogs(nombre=info["nombre"], edad=info["edad"], fecha_nacimiento=info["fecha_nacimiento"])
            perro.save()
            mensaje = f"Se creó el perro {perro.nombre}"
        else:
            return render(request, "start/createdogs.html", {"formulario": formulario})

    formulario = CreateDogsForm()
    return render(request, "start/createdogs.html", {"formulario": formulario, "mensaje": mensaje})

def createbirds(request):
    mensaje = "Aquí puedes crear un pájaro"

    if request.method == "POST":
        formulario = CreateBirdsForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            pajaro = Birds(nombre=info["nombre"], edad=info["edad"], fecha_nacimiento=info["fecha_nacimiento"])
            pajaro.save()
            mensaje = f"Se creó el pájaro {pajaro.nombre}"
        else:
            return render(request, "start/createbirds.html", {"formulario": formulario})

    formulario = CreateBirdsForm()
    return render(request, "start/createbirds.html", {"formulario": formulario, "mensaje": mensaje})

def search(request):
    termino = request.POST.get("termino")
    if termino:
        # Realiza la búsqueda usando el término ingresado por el usuario
        # y muestra los resultados
        animales = Cats.objects.filter(nombre__icontains=termino) | Dogs.objects.filter(nombre__icontains=termino) | Birds.objects.filter(nombre__icontains=termino)
        return render(request, "start/search.html", {"animales": animales})
    else:
        # Muestra un mensaje de error si el formulario no es válido
        return render(request, "start/search.html", {"mensaje": "No se ingresó ningún término de búsqueda"})

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cats, Dogs, Birds
from .forms import CreateCatsForm, CreateDogsForm, CreateBirdsForm
from django.utils.translation import gettext as _
from django.views.generic import ListView
from .forms import searchForm
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import get_object_or_404

def some_view(request):
    translated_text = _('Texto a traducir')
# Create your views here.

def aboutus(request):
    return render ( request, 'start/aboutus.html')


def StarterApp (request):
    return render(request, 'start/start.html')
    
def createcats(request):
    mensaje = "Aquí puedes crear un gato"

    if request.method == "POST":
        formulario = CreateCatsForm(request.POST,request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            gato = Cats(nombre=info["nombre"], edad=info["edad"], fecha_nacimiento=info["fecha_nacimiento"], imagen=info["imagen"],texto_formateado=info["texto_formateado"])
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
    if request.method == 'GET':
        termino = request.GET.get('termino', '')
        form = searchForm(initial={'termino': termino})
        results = None

        if termino:
            # Use Q object for filtering multiple fields
            dogs_results = Dogs.objects.filter(Q(nombre__icontains=termino) | Q(edad__icontains=termino))
            birds_results = Birds.objects.filter(Q(nombre__icontains=termino) | Q(edad__icontains=termino))
            cats_results = Cats.objects.filter(Q(nombre__icontains=termino) | Q(edad__icontains=termino))

            # Combine the results into a list
            results = list(dogs_results) + list(birds_results) + list(cats_results)
        else:
            # Display all results when no search term is provided
            dogs_results = Dogs.objects.all()
            birds_results = Birds.objects.all()
            cats_results = Cats.objects.all()
            results = list(dogs_results) + list(birds_results) + list(cats_results)

        return render(request, 'start/search.html', {'form': form, 'results': results})

    return HttpResponseNotAllowed(['GET'])


def deletecat(request, pk):
    gato = get_object_or_404(Cats, pk=pk)
    if request.method == "POST":
        gato.delete()
        return HttpResponseRedirect(reverse('StarterApp:StarterApp'))
    return render(request, 'start/deletecat.html', {'animal': gato})

def deletedog(request, pk):
    perro = get_object_or_404(Dogs, pk=pk)
    if request.method == "POST":
        perro.delete()
        return HttpResponseRedirect(reverse('StarterApp:StarterApp'))
    return render(request, 'start/deletedog.html', {'animal': perro})

def deletebird(request, pk):
    pajaro = get_object_or_404(Birds, pk=pk)
    if request.method == "POST":
        pajaro.delete()
        return HttpResponseRedirect(reverse('StarterApp:StarterApp'))
    return render(request, 'start/deletebird.html', {'animal': pajaro})


    
def editcat(request, pk):
    gato = get_object_or_404(Cats, pk=pk)
    
    if request.method == 'POST':
        formulario = CreateCatsForm(request.POST, request.FILES)
        if formulario.is_valid():
            gato.nombre = formulario.cleaned_data.get('nombre')
            gato.edad = formulario.cleaned_data.get('edad')
            gato.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
            gato.imagen = formulario.cleaned_data.get('imagen')  # Actualizar la imagen
            gato.texto_formateado = formulario.cleaned_data.get('texto_formateado')  # Actualizar el texto formateado
            gato.save()
            return redirect('StarterApp:StarterApp')
    else:
        formulario = CreateCatsForm(initial={
            'nombre': gato.nombre,
            'edad': gato.edad,
            'fecha_nacimiento': gato.fecha_nacimiento,
            'imagen': gato.imagen,  # Cargar la imagen actual
            'texto_formateado': gato.texto_formateado,  # Cargar el texto formateado actual
        })

    return render(request, 'start/editcat.html', {'formulario': formulario, 'animal': gato})


def editbird(request, pk):
    pajaro = get_object_or_404(Birds, pk=pk)
    
    if request.method == 'POST':
        formulario = CreateBirdsForm(request.POST)
        if formulario.is_valid():
            pajaro.nombre = formulario.cleaned_data.get('nombre')
            pajaro.edad = formulario.cleaned_data.get('edad')
            pajaro.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
            pajaro.save()
            formulario.save()
            return redirect('StarterApp:StarterApp')
    else:
        formulario = CreateBirdsFormForm(initial={'nombre': pajaro.nombre, 'edad': pajaro.edad, 'fecha_nacimiento': pajaro.fecha_nacimiento})

    return render(request, 'start/editbird.html', {'formulario': formulario, 'animal':pajaro})

def editdog(request, pk):
    perro = get_object_or_404(Dogs, pk=pk)

    if request.method == 'POST':
        formulario = CreateDogsForm(request.POST)
        if formulario.is_valid():
            perro.nombre = formulario.cleaned_data.get('nombre')
            perro.edad = formulario.cleaned_data.get('edad')
            perro.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
            perro.save()
            return redirect('StarterApp:StarterApp')
    else:
        formulario = CreateDogsForm(initial={'nombre': perro.nombre, 'edad': perro.edad, 'fecha_nacimiento': perro.fecha_nacimiento})

    return render(request, 'start/editdog.html', {'formulario': formulario, 'animal':perro})









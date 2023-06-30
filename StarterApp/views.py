from django.shortcuts import render
from StarterApp.forms import createcatsFormulario
from StarterApp.models import Cats

# Create your views here.

def StarterApp (request):
    return render(request, 'start/start.html')
    
def createcats(request):
    mensaje = "Aquí puedes crear un gato"

    if request.method == "POST":
        formulario = createcatsFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            gato = Cats(nombre=info["nombre"], edad=info["edad"], fecha_nacimiento=info["fecha_nacimiento"])
            gato.save()
            mensaje = f"Se creó el gato {gato.nombre}"
        else:
            return render(request, "start/createcats.html", {"formulario": formulario})

    formulario = createcatsFormulario()
    return render(request, "start/createcats.html", {"formulario": formulario, "mensaje": mensaje})



from django.shortcuts import render
from StarterApp.forms import createcatsFormulario
from StarterApp import Cats

# Create your views here.

def StarterApp (request):
    return render(request, 'start/start.html')
    
def createcats(request):

    if request.method == "POST":
        formulario = createFormlario(request.POST)
        if formulario.is_valid ():
            info = formulario.cleaned_data
            gato = Cats (nombre= info["nombre"],edad= info["edad"], fecha_nacimiento= ["fecha_nacimiento"],)
            gato.save ()
            mensaje: f"Se creo el gato {gato.nombre}"
        else: 
            return render (request, "StarterApp/createcats.html", {"formulario": formulario} )

    formulario= createcatsFormulario ()
    return render (request, "StarterApp/createcats.html", {"formulario": formulario, "mensaje": mensaje})


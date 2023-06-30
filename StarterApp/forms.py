from django import forms

class createcatsFormulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    edad= forms.IntegerField()
    fecha_naciemiento= forms.DateField ()
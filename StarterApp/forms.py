from django import forms


class CreateCatsForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=['%d/%m/%Y'])

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data['fecha_nacimiento']
        return fecha

class CreateDogsForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=['%d/%m/%Y'])

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data['fecha_nacimiento']
        return fecha

class CreateBirdsForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=['%d/%m/%Y'])

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data['fecha_nacimiento']
        return fecha

class searchForm(forms.Form):
    termino = forms.CharField(label='Buscar')




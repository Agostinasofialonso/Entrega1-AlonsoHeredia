from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Cats(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    imagen = models.ImageField(upload_to='cat_images', blank=True,null=True)
    texto_formateado = RichTextField(blank=True, null=True)


    @property
    def fecha_nacimiento_formatted(self):
        return self.fecha_nacimiento.strftime('%d/%m/%Y')

    def get_edit_url(self):
        return reverse('StarterApp:editcat', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('StarterApp:deletecat', args=[str(self.id)])

class Dogs(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    @property
    def fecha_nacimiento_formatted(self):
        return self.fecha_nacimiento.strftime('%d/%m/%Y')

    def get_edit_url(self):
        return reverse('StarterApp:editdog', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('StarterApp:deletedog', args=[str(self.id)])

class Birds(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    @property
    def fecha_nacimiento_formatted(self):
        return self.fecha_nacimiento.strftime('%d/%m/%Y')

    def get_edit_url(self):
        return reverse('StarterApp:editbird', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('StarterApp:deletebird', args=[str(self.id)])



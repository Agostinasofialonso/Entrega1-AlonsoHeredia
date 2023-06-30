from django.db import models

# Create your models here.
class Cats(models.Model): 
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    @property
    def fecha_nacimiento_formatted(self):
        return self.fecha_nacimiento.strftime('%d/%m/%Y')

    

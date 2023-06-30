from django.db import models

# Create your models here.
class Cats(models.Model): 
    name= models.CharField(max_length=20)
    edad= models.IntegerField ()
    fecha_nacimiento= models.DateField ()
    

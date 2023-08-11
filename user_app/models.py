from django.db import models
from django.contrib.auth.models import user

class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fechaNacimiento = models.DateField(blank=True, null=True)
# Create your models here.

from django.contrib import admin

# Register your models here.
from .models import Cats, Dogs, Birds

admin.site.register(Cats)
admin.site.register(Dogs)
admin.site.register(Birds)


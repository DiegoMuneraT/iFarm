from django.contrib import admin
from .models import Cultivo, Usuario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Cultivo)
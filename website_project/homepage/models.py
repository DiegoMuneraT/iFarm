from django.db import models

# Create your models here.
# Data coordination.

#Creación de la clase Usuario
class Usuario(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    correo = models.EmailField(max_length=100)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.correo)
    
#Creación de la clase Cultivo
class Cultivo(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to = "staticfiles/images/")
    
    def __str__(self):
        texto ="{0} ({1})"
        return texto.format(self.nombre,  self.tipo)
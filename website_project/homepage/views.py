from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Cultivo
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

# HOME PAGE
@login_required
def home(request):
    cultivosLista = Cultivo.objects.all()
    return render(request, 'homepage/home.html', {"cultivos": cultivosLista})

def signForm(request):
    return render(request, 'homepage/signup.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']    
        
        myuser = User.objects.create_user(username, email, pass1)    
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Tu cuenta ha sido creada satisfactoriamente")
        
        return redirect('login')

# REGISTER PLANT
def registrarCultivo(request):
    nombre = request.POST['txtNombre']
    tipo = request.POST['txtTipo']
    imagen = request.POST['imgFoto']
    cultivo = Cultivo.objects.create(nombre=nombre, tipo=tipo, imagen=imagen)
    return render(request, "homepage/cultivoCreado.html")

# MODIFY 
def modificarCultivo(request, nombre):
    cultivo = Cultivo.objects.get(nombre=nombre)
    return render(request, "homepage/modCultivo.html", {"cultivo": cultivo})

def modificacion(request):
    nombre = request.POST['txtNombre']
    tipo = request.POST['txtTipo']
    imagen = request.POST['imgFoto']
    
    cultivo = Cultivo.objects.get(nombre=nombre)
    cultivo.nombre = nombre
    cultivo.tipo = tipo
    cultivo.imagen = imagen
    #cultivo.imagen = imagen
    cultivo.save()
    return redirect('/home')

# STATICS
def infoCultivo(request): #, nombre
    #cultivo = Cultivo.objects.get(nombre=nombre)
    cultivosLista = Cultivo.objects.all()
    return render(request, "homepage/statics.html", {"cultivos": cultivosLista})

# DELETE
def eliminarCultivo(request, nombre):
    cultivo = Cultivo.objects.get(nombre=nombre)
    cultivo.delete()
    return render(request, "homepage/cultivoEliminado.html")
        
# WIKI
def wiki(request):
    return render(request, "homepage/wiki.html")

def read(request):
    return render(request, "homepage/read.html")

#--THESE WILL ACTIVATE WATER FUNCTION WHEN DEVICE IS BUILT--
def activarRiego(request):
    #cultivo = Cultivo.objects.get(nombre=nombre)
    return render(request, "homepage/waterOn.html") # ,{"cultivo": cultivo}
    
def desactivarRiego(request):
    #cultivo = Cultivo.objects.get(nombre=nombre)
    return render(request, "homepage/waterOff.html") # ,{"cultivo": cultivo}


    """ 
    """
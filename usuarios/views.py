from django.shortcuts import render, redirect
from .models import Usuario

def lista_usuarios(request):
    usuario = Usuario.objects.all()
    return render(request,"usuarios/lista.html",{"usuarios":usuario})

def crear_usuario(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")

        if nombre:
            Usuario.objects.create(nombre = nombre)
            return redirect("/")
    
    return render(request,("usuarios/crear.html"))

def eliminar_usuario(request,id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect("/")
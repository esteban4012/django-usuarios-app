from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def lista_usuarios(request):
    usuario = Usuario.objects.all()
    return render(request,"usuarios/lista.html",{"usuarios":usuario})

def crear_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = UsuarioForm()    
    return render(request,"usuarios/crear.html", {"form":form})

def eliminar_usuario(request,id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect("/")


def editar_usuario(request,id):
    usuario = Usuario.objects.get(id=id)
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        if nombre:
            usuario.nombre = nombre
            usuario.save()
            return redirect("/")
    return render(request,"usuarios/editar.html", {"usuario" : usuario})
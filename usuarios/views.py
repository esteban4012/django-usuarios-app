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


def editar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuarios/editar.html', {'form': form})
from django.urls import path
from . import views

urlpatterns = [
    path("",views.lista_usuarios),
    path("crear/",views.crear_usuario),
]

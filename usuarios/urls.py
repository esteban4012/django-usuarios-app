from django.urls import path
from . import views

urlpatterns = [
    path("",views.lista_usuarios),
    path("crear/",views.crear_usuario),
    path("eliminar/<int:id>/",views.eliminar_usuario),
    path("editar/<int:id>/", views.editar_usuario),
]

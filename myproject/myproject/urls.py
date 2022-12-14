"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, mostrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, 
                            mostrar_mascotas, BuscarMascota, AltaMascota, ActualizarMascota, BorrarMascota,
                            mostrar_empleos, BuscarEmpleo, AltaEmpleo, ActualizarEmpleo, BorrarEmpleo,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), #ESTA ES LA FUNCION SALUDAR QUE CREAMOS PRIMERO
    path('mi-familia/', mostrar_familiares), #NUEVA VISTA
    path('mi-familia/buscar', BuscarFamiliar.as_view()), #ESTA RUTA BUSCA FAMILIAR POR NOMBRE
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mis-mascotas/', mostrar_mascotas),
    path('mis-mascotas/buscar', BuscarMascota.as_view()),
    path('mis-mascotas/alta', AltaMascota.as_view()),
    path('mis-mascotas/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('mis-mascotas/borrar/<int:pk>', BorrarMascota.as_view()),
    path('mis-empleos/', mostrar_empleos),
    path('mis-empleos/buscar', BuscarEmpleo.as_view()),
    path('mis-empleos/alta', AltaEmpleo.as_view()),
    path('mis-empleos/actualizar/<int:pk>', ActualizarEmpleo.as_view()),
    path('mis-empleos/borrar/<int:pk>', BorrarEmpleo.as_view()),
]

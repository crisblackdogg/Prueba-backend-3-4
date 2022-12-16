"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appPrueba import views

urlpatterns = [
    path('', views.inicio),
    # crud
    path('listado/', views.listaInscripciones),
    path('agregar_inscripcion/', views.crearInscripcion),
    path('eliminar/<int:id>', views.eliminarInscripcion),
    path('actualizar/<int:id>', views.actualizarInscripcion),
    # CBV
    path('inscripciones_class/', views.Listado.as_view()),
    path('inscripciones_class/<int:pk>', views.detalle.as_view()),
    # FBV
    path('instituciones_fun/', views.INST_LIST),
    path('instituciones_fun/<int:id>', views.INST_DETALLE),
    # api
    path('inscripciones_api/', views.apiInscription),

]
from django.shortcuts import render,redirect
# from django_seminario_app.models import Inscripcion
from appPrueba.forms import Form_Inscript
from .serialiazers import InscripcionSE , InstitucionSE
from .models import Inscripcion, Institucion
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404
from django.http import JsonResponse
# INDEX

def inicio(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'inscripcion.html')
    
# API
def apiInscription(request):
    inscript = Inscripcion.objects.all()
    data = {'Inscripciones' : list(inscript.values('rut','nombre','telefono','fechaInscripcion','hora','institucion','estadoReserva','observacion'))}
    return JsonResponse(data)

# CRUD
def listaInscripciones(request):
    listInscripcion = Inscripcion.objects.all()
    data = {'inscripciones': listInscripcion}
    return render(request, 'inscripcion.html', data)

def crearInscripcion(request):
    form = Form_Inscript()
    if request.method == 'POST':
        form = Form_Inscript(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'add_inscripcion.html', data)

def eliminarInscripcion(request,id):
    joel = Inscripcion.objects.get(id = id)
    joel.delete()
    return redirect('/')

def actualizarInscripcion(request,id):
    joel = Inscripcion.objects.get(id = id)
    form = Form_Inscript(instance=joel)
    if request.method == 'POST':
        form = Form_Inscript(request.POST, instance=joel)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,'add_inscripcion.html',data)

# CBV

class Listado(APIView):
    def get(self, request):
        inscripciones = Inscripcion.objects.all()
        serial = InscripcionSE(inscripciones, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscripcionSE(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class detalle(APIView):
    def get_object(self, pk):
        try:
            return Inscripcion.objects.get(id=pk)
        except Inscripcion.DoesNotExist:
            return Http404

    def get(self, request, pk):
        inscripcion = self.get_object(pk)
        serial = InscripcionSE(inscripcion)
        return Response(serial.data)

    def put(self, request, pk):
        inscripcion = self.get_object(pk)
        serial = InscripcionSE(inscripcion, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscripcion = self.get_object(pk)
        inscripcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# FBV

@api_view(['GET','POST'])
def INST_LIST (request):
    if request.method == 'GET':
        institucion = Institucion.objects.all()
        serial = InstitucionSE(institucion , many=True)
        return Response(serial.data)

    elif request.method == 'POST':
        serial = InstitucionSE(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
def INST_DETALLE(request,id):
    try:
        institucion = Institucion.objects.get(pk = id)
    except institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSE(institucion)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSE(institucion,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
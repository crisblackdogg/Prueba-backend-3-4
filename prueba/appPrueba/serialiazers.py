from rest_framework import serializers
from appPrueba.models import Inscripcion, Institucion

class InscripcionSE(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'

class InstitucionSE(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'
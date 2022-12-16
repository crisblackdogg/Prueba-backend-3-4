from dataclasses import fields
from django import forms
from appPrueba.models import Inscripcion



class Form_Inscript(forms.ModelForm):
    class Meta:
        model   = Inscripcion
        fields = '__all__'
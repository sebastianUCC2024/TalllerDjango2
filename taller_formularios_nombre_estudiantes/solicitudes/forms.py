from django import forms
from .models import Solicitudes

class SolicitudesForm(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = '__all__'
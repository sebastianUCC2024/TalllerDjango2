from django import forms
from .models import Solicitudes


class SolicitudesForms(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = '__all__'
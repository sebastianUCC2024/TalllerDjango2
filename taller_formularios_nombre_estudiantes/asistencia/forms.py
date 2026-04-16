from django import forms
from .models import Asistencia
from django.utils import timezone


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        widgets = {
            'fechaAsistencia': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'horaIngreso': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'horaSalida': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aceptar formatos comunes para fecha en parsing
        self.fields['fechaAsistencia'].input_formats = ['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y']
        # Si no viene valor inicial, poner hoy
        if not self.initial.get('fechaAsistencia') and not (self.instance and self.instance.fechaAsistencia):
            self.initial['fechaAsistencia'] = timezone.localdate().strftime('%Y-%m-%d')
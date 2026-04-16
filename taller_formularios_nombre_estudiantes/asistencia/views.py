from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AsistenciaForm
from .models import Asistencia
from django.shortcuts import get_object_or_404
from django.utils import timezone

def asistencia_create(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            asistencia = form.save(commit=False)
            # Si no se proporcionó fecha, usar hoy
            if not asistencia.fechaAsistencia:
                asistencia.fechaAsistencia = timezone.localdate()
            asistencia.save()
            return redirect('asistencia_success')
    else:
        form = AsistenciaForm()

    return render(request, 'asistencia/formulario.html', {'form': form})


def asistencia_success(request):
    return render(request, 'asistencia/success.html')


def listar_asistencias(request):
    asistencias = Asistencia.objects.all().order_by('-fechaAsistencia')
    return render(request, 'asistencia/lista.html', {'asistencias': asistencias})


def detalle_asistencia(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    return render(request, 'asistencia/detalle.html', {'asistencia': asistencia})
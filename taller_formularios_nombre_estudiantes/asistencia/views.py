from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AsistenciaForm

def asistencia_create(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencia_success')
    else:
        form = AsistenciaForm()

    return render(request, 'asistencia/formulario.html', {'form': form})


def asistencia_success(request):
    return render(request, 'asistencia/success.html')
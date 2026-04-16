from django.shortcuts import render, redirect
from .forms import SolicitudesForm

def solicitud_create(request):
    if request.method == 'POST':
        form = SolicitudesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('solicitud_success')
    else:
        form = SolicitudesForm()

    return render(request, 'solicitudes/formulario.html', {'form': form})


def solicitud_success(request):
    return render(request, 'solicitudes/success.html')
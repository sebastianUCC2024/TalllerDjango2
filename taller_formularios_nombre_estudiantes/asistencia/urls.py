from . import views
from django.urls import path

urlpatterns = [
    path("nuevo/", views.asistencia_create, name="asistencia_new"),
    path("exito/", views.asistencia_success, name="asistencia_success"),
]
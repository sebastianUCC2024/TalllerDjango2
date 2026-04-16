from django.urls import path
from .views import solicitud_create, solicitud_success

urlpatterns = [
    path('nuevo/', solicitud_create, name='solicitud_new'),
    path('exito/', solicitud_success, name='solicitud_success'),
]
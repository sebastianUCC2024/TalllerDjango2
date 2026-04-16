from django.contrib import admin
from .models import Solicitudes


@admin.register(Solicitudes)
class SolicitudesAdmin(admin.ModelAdmin):
	list_display = ('nombreSolicitante', 'documentoIdentidad', 'correoElectronico', 'telefonoContacto', 'fechaSolicitud')
	search_fields = ('nombreSolicitante', 'documentoIdentidad', 'correoElectronico')

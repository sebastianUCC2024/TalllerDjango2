from django.contrib import admin
from .models import Asistencia


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
	list_display = ('nombreCompleto', 'documentoIdentidad', 'correoElectronico', 'fechaAsistencia', 'presente')
	search_fields = ('nombreCompleto', 'documentoIdentidad', 'correoElectronico')
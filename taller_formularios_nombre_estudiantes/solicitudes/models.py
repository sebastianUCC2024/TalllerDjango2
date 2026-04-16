from django.db import models

# Create your models here.
class Solicitudes(models.Model):
    nombreSolicitante = models.CharField(max_length=150)
    documentoIdentidad = models.CharField(max_length=50)
    correoElectronico = models.EmailField()
    telefonoContacto = models.IntegerField()
    asusto = models.CharField(max_length=100)
    descripcionDetallada = models.CharField(max_length=200)
    fechaSolicitud = models.DateTimeField()
    archivoAdjunto = models.FieldFile(upload_to='archivos/',null=True,blank=True)
    
    def __str__(self):
        return f"{self.nombreSolicitante} - {self.documentoIdentidad} - {self.correoElectronico} - {self.telefonoContacto} - {self.asusto} - {self.descripcionDetallada} - {self.fechaSolicitud} - {self.archivoAdjunto}"
    


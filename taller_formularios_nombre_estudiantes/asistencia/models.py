from django.db import models

class Asistencia(models.Model):
    nombreCompleto = models.CharField(max_length=150)
    documentoIdentidad = models.CharField(max_length=50)
    correoElectronico = models.EmailField()
    fechaAsistencia = models.DateField()
    horaIngreso = models.TimeField()
    horaSalida = models.TimeField()
    presente = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.nombreCompleto} - {self.documentoIdentidad} - {self.correoElectronico} - {self.fechaAsistencia} - {self.horaIngreso} - {self.horaSalida} - {'Presente' if self.presente else 'Ausente'} - {self.observaciones}"
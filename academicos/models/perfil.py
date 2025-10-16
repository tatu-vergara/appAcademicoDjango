from django.db import models
from .estudiante import Estudiante

class PerfilEstudiante(models.Model):
    estudiante = models.OneToOneField(
        Estudiante,
        on_delete=models.CASCADE,
        related_name="perfil"
    )
    biografia = models.TextField(blank=True)
    foto = models.ImageField(upload_to="perfiles/", blank=True, null=True)
    redes = models.JSONField(blank=True, null=True)  # usar TextField si tu MySQL no soporta JSON

    def __str__(self):
        return f"Perfil de {self.estudiante}"

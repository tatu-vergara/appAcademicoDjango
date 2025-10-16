from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

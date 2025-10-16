from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    especialidad = models.CharField(max_length=120, blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} <{self.email}>"

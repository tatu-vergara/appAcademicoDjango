from django.db import models
from .profesor import Profesor
from .estudiante import Estudiante

class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.CASCADE,
        related_name="cursos",
    )
    # Declaramos aquí la M2M usando la through Inscripcion (string para evitar orden de importación)
    estudiantes = models.ManyToManyField(
        Estudiante,
        through="Inscripcion",
        related_name="cursos",
    )

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} (Prof. {self.profesor.nombre})"

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .estudiante import Estudiante
from .curso import Curso

class EstadoInscripcion(models.TextChoices):
    ACTIVO = "ACT", "Activo"
    FINALIZADO = "FIN", "Finalizado"

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name="inscripciones",
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="inscripciones",
    )
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=3,
        choices=EstadoInscripcion.choices,
        default=EstadoInscripcion.ACTIVO,
    )
    nota_final = models.DecimalField(
        max_digits=5, decimal_places=2,
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        unique_together = [("estudiante", "curso")]
        ordering = ["-fecha_inscripcion"]

    def __str__(self):
        return f"{self.estudiante} → {self.curso} ({self.estado})"

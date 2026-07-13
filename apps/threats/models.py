import uuid

from django.db import models


class Threat(models.Model):
    class RiskLevel(models.TextChoices):
        LOW = "LOW", "Bajo"
        MEDIUM = "MEDIUM", "Medio"
        HIGH = "HIGH", "Alto"
        CRITICAL = "CRITICAL", "Crítico"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField()

    owasp_category = models.CharField(
        max_length=150
    )

    recommendation = models.TextField()

    risk_level = models.CharField(
        max_length=10,
        choices=RiskLevel.choices,
        default=RiskLevel.MEDIUM
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
    
    
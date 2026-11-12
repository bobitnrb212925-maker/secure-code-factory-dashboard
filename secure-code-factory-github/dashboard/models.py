
from django.db import models


class SITFPillar(models.Model):

    PILLAR_CHOICES = [
        ('Endpoint/IDE', 'Endpoint/IDE'),
        ('VCS', 'Version Control System'),
        ('CI/CD', 'CI/CD'),
        ('Registry', 'Registry'),
        ('Production', 'Production'),
    ]

    name = models.CharField(
        max_length=100,
        unique=True,
        choices=PILLAR_CHOICES
    )

    description = models.TextField()

    def __str__(self):
        return self.name


class SecurityFinding(models.Model):

    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    pillar = models.ForeignKey(
        SITFPillar,
        on_delete=models.PROTECT,
        related_name='findings'
    )
    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

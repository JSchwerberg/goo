from django.db import models

# Create your models here.

class InstallCommand(models.Model):
    device = models.CharField(max_length=32)
    command = models.TextField()
    status = models.BooleanField(default=True)

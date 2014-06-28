from django.db import models

class Config(models.Model):
	key = models.CharField(max_length=32, unique=True)
	value = models.TextField()


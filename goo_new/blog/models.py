from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    updated = models.BooleanField(default=False)
    modified = models.DateTimeField(null=True, blank=True)
    


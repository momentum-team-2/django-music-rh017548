from django.db import models
from django import forms
from PIL import Image


# Create your models here.

class Albums(models.Model):
    albumcover = models.URLField(max_length=255, null= True)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class MovieModel(models.Model):
    moviename = models.CharField(max_length=50)
    hero = models.CharField(max_length=50)
    heroien = models.CharField(max_length=50)
    releasedate = models.DateField()
    rating = models.IntegerField()
    

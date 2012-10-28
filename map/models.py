from django.db import models

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    x_position = models.IntegerField()
    y_position = models.IntegerField()

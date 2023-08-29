from django.db import models

# Create your models here.

class FeaturesModel(models.Model):
    age = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    k = models.IntegerField()
from django.db import models

# Create your models here.

class fruit(models.Model):

    name = models.CharField(max_length=10)
    price = models.IntegerField()
    units = models.IntegerField()

from django.db import models

# Create your models here.

class Mibayashi(models.Model):
    name = models.CharField(max_length=128)

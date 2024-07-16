
from django.db import models

class User (models.Model):
  Name = models.CharField(max_length=100)
  Email = models.EmailField(max_length=50)
  Address =models.CharField( max_length=100)
  Age = models.IntegerField()



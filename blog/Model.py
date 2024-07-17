
from django.db import models
class User (models.Model):
  gender_field=[
    ('male','Male'),
    ('female','Female'),
  ]
  Name = models.CharField(max_length=100)
  Email = models.EmailField(max_length=50)
  Address =models.CharField( max_length=100)
  Age = models.IntegerField()
  Gender = models.CharField(max_length=50,choices=gender_field)
  Country= models.CharField(max_length=100)




from django.db import models
class user(models,models):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50 ,unique=True)
    address =models.CharField( max_length=100)
    age = models.IntegerField()

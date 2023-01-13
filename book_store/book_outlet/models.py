from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=40)
    rating = models.IntegerField()
    

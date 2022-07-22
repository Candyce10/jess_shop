from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

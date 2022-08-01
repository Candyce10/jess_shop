from django.db import models
from django.urls import reverse

class Product(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=1000)
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['name']

from django.db import models
from django.urls import reverse
from django.conf import settings

class Product(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    price = models.FloatField(null=True)
    description = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=1000)
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['name']


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
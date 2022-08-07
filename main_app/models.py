from pyexpat import model
from django.db import models
from django.forms import CharField
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    price = models.FloatField(null=True)
    description = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=1000)
    slug = models.SlugField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['name']



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_subtotal(self):
        orderitems = self.orderproduct_set.all()
        total = sum([item.get_total for item in orderitems]) 
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderproduct_set.all()
        subtotal = sum([item.get_total for item in orderitems]) 
        total = subtotal + 20
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderproduct_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address





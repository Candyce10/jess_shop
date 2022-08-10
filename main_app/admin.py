from django.contrib import admin
from .models import Customer, Product, Order, OrderProduct, ShippingAddress, BillingAddress

admin.site.register(Product) 
admin.site.register(Order) 
admin.site.register(OrderProduct)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(BillingAddress)

from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from .models import *
from django.views.generic import DetailView
import json

class Home(View):
    def get(self, request):
        return HttpResponse("Gainzz & Curvezz Home")

class Home(TemplateView):
    template_name = "home.html"


class About(View):
    def get(self, request):
        return HttpResponse("Gainzz & Curvezz About")

class About(TemplateView):
    template_name = "about.html"


class FAQ(View):
    def get(self, request):
        return HttpResponse("Gainzz & Curvezz FAQ")

class FAQ(TemplateView):
    template_name = "FAQ.html"



class ProductList(TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all() 
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'get_cart_subtotal': 0}
    context = {'items':items, 'order':order}
    return render(request, "cart.html", context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'get_cart_subtotal': 0}
    context = {'items':items, 'order':order}
    return render(request, "checkout.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete = False)

    orderItem, created = OrderProduct.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if order.quantity <=0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe = False)



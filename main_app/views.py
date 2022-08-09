from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import *
from django.views.generic import DetailView


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




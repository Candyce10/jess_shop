from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Product
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



class ProductList(TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all() 
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"
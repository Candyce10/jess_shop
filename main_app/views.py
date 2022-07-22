from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView


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


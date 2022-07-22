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

 #adds artist class for mock database data
class Product:
    def __init__(self, name, image, bio, ingredients):
        self.name = name
        self.image = image
        self.bio = bio
        self.ingredients = ingredients


products = [
  Product("Gummies", "https://i.imgur.com/Ue5dO1E.jpg",
          "Gummies are created with pure natural ingredients formulated to help enhance your butt and hip size safely. This product contains  a group of carefully-selected natural ingredients, vitamins, minerals and herbs combined together to enhance the size and shape of your lower body parts and to enhance your curves.", "Gummies blend: 1036mg, fenugreek seed, fennel seed, wild Mexican yam(root), blessed thistle (whole herb), dong plant Maca root and other ingredients, Google  Ethis ingridents to see how natural they are and what they do to the body."),
  Product("APETI TABLETS",
          "https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png", "APETI tablets contain only Cyproheptadine but no Lysine as Apetamin has. Taken alone they will stimulate your appetite and allow you to eat larger meals. The side effects of taking these tablets are drowsiness and somnolence. Many people who initially complain of drowsiness usually no longer do so after three or four days of continuous use.  Apeti tablets are to be taken by mouth either with or without water. Take one tablet before food three times a day. For better results you can pair these tablets with the Apetamin syrup.", "Each tablet contains: Cyproheptadine Hydrochloride (anhydrous) BP 4mg, Thiamine Hydrochloride (Vitamin B1) BP 1.5mg, Riboflavin (Vitamin B2) BP 1.5mg, Pyridoxine Hydrochloride (Vitamin B6) BP 1mg, Calcium Pantothenate BP 2.5mg"),
  Product("Joji", "https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png",
          "Are you skinny, thin, slim, or you are not happy with your body small size? There it goes Super Apeti plus Syrup is indicated for loss of appetite, weight loss, anorexia nervosa and as an adjunct to antitubercular and antiretroviral regimens for weight gain. Gain 8-10 pounds in 1 week. Take syrup 3x a day 30 minutes before each meal. (10-15ML).", "Contains a unique combination of Cyproheptadine, Lysine and Vitamins."),

]

class ProductList(TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = products 
        return context

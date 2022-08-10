from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from .models import *
from django.views.generic import DetailView
import json





def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'get_cart_subtotal': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, "home.html", context)



def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'get_cart_subtotal': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, "about.html", context)


    
def faq(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'get_cart_subtotal': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, "FAQ.html", context)





def products(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'get_cart_subtotal': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, "product_list.html", context)


class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'get_cart_subtotal': 0}
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, "cart.html", context)




def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'get_cart_subtotal': 0}
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
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

    if orderItem.quantity <=0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe = False)



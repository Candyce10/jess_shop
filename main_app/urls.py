from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('FAQs/', views.faq, name="FAQ"),
    path('products/', views.products, name="product_list"),
    path('products/<slug:slug>/', views.ProductDetail.as_view(), name="product_detail"),
    path('cart/', views.cart, name="cart"),
    path('cart/checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    
]

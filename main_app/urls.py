from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('FAQs/', views.FAQ.as_view(), name="FAQ"),
    path('products/', views.ProductList.as_view(), name="product_list"),
    path('products/<slug:slug>/', views.ProductDetail.as_view(), name="product_detail"),
]

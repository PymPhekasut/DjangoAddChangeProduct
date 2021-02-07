#urls.py

from django.urls import path, include 
from .views import Home, About, Contact, Garden, AddProduct, Product
#import home function

urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
    path('contact/', Contact, name='contact-page'),
    path('garden/', Garden, name='garden-page'),
    path('addproduct/', AddProduct, name='addproduct-page'),
    path('allproduct/', Product, name='allproduct-page'),
]
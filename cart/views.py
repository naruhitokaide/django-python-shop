from django.http import HttpResponse
from django.shortcuts import render
from .models import Cart

from shop.models import Product

def add_cart(request, id):
    if request.POST:
        product = Product.objects.get(id = id)
        print(Cart.objects.filter(device = request.COOKIES['device'], product=product, quantity=1).exists())
        print("Already In Cart")
        print(product.price)
    return HttpResponse(request.COOKIES['device'])

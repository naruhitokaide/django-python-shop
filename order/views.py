from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Cart
from shop.models import Product

def cart(request, id):
    if request.POST:
        product = Product.objects.get(id = id)
        cart = Cart.objects.filter(device = request.COOKIES['device'], product = product)
        if cart.exists():
            return HttpResponse("Product Already In Cart")
        else:
            Cart(
                product = product, 
                quantity = request.POST['quantity'], 
                device = request.COOKIES['device']
                ).save()
            print("Product Added")
            return redirect(request.META.get("HTTP_REFERER"))
    return HttpResponse(cart)

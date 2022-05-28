from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Cart
from shop.models import Product
from .cart import Cart

def cart(request, id):
    if request.POST:
        product = Product.objects.get(id = id)
        request.session[str(product.id)] = product.id
        cart = Cart(request = request)

        print(len(request.session['s_key']))
    return HttpResponse(request.session.items())

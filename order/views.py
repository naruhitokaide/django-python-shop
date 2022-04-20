from django.shortcuts import render
from django.http import HttpResponse

from .models import Cart

def cart(request, id):
    if request.POST:
        if Cart.objects.filter(device = request.COOKIES['device']).exists():
            return HttpResponse("Not Valid")
        else:
            return HttpResponse("Valid")
    return HttpResponse(cart)
        
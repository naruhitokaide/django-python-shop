from django.http import HttpResponse
from django.shortcuts import render

def add_cart(request):
    return HttpResponse(request.COOKIES['device'])

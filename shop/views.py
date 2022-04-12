from . models import Brand, Category, Product
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'categories': Category.objects.all(),
        # 'products': Paginator(Product.objects.all(), 8).page(1)
        'products': Product.objects.all()[:8]
    }
    return render(request, 'home.html', context)


def product_list(request):

    context = {
        'categories': Category.objects.all(),
        'brands': Brand.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'productList.html', context)
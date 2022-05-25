from . models import Brand, Category, Product
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
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


def productdetail(request, id):
    product = Product.objects.get(pk = id)
    context = {
        'product':product,
        'similar' : Product.objects.filter(category = product.category) 
    }
    print(product.images.all())
    return render(request, 'detailVIew.html', context)
    
    
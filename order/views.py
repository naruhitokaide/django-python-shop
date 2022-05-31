from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from order.cart import Cart
from shop.models import Product

def cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        productid = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id = productid)
        cart.add(product, product_qty)
        return JsonResponse({'qty':cart.__len__()})

def cart_list(request):
    cart = Cart(request)
    return render(request, 'cartList.html')
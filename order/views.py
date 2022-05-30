from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.sessions.models import Session


from order.cart import Cart
from shop.models import Product

def cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        productid = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id = productid)
        cart.add(product, product_qty)
        s = Session.objects.get(pk = 'kd4pvykt3fyxr1ydb6zvt7ll9hwg2bit')
        print(s.get_decoded())
        return JsonResponse({'qty':product_qty})
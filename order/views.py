from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.sessions.models import Session


from order.cart import Cart
from shop.models import Product

def cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        productid = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id = productid)
        cart.add(product)
        s = Session.objects.get(pk = 'dgv0atfmvudpc23o3khfm560rahf9rmf')
        print(s.get_decoded())
        return JsonResponse({'data':'product sent to cart.py'})
from decimal import Decimal
from django.contrib.sessions.models import Session

from shop.models import Product

class Cart():

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('s_key')
        if 's_key' not in request.session:
            cart = self.session['s_key'] = {}
        self.cart = cart


    def add(self, product, product_qty):
        product_id = product.id
        if str(product_id) not in self.cart:
            self.cart[product_id] = {'price':product.price, 'qty': product_qty}

        elif str(product_id) in self.cart:
            pass
        self.session.modified = True


    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['sub_total'] = Decimal(item['price']) * Decimal(item['qty'])
            yield item


    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())


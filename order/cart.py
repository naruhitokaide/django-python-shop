from decimal import Decimal
from django.contrib.sessions.models import Session
from requests import request, session

from shop.models import Product

class Cart():

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('s_key')
        if 's_key' not in request.session:
            cart = self.session['s_key'] = {}
        self.cart = cart


    def add(self, product, product_qty):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'price':product.price, 'qty': product_qty}
        # for updating product quantity in session
        elif product_id in self.cart:
            self.cart[product_id]['qty'] += product_qty
            print(self.__len__())
        self.save()


    def remove(self, product_id):
        if product_id in self.cart:
            print(type(product_id))
            del self.cart[product_id]
            self.save()

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


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())


    def single_qty(self, product_id):
        self.product_id = str(product_id)
        if self.product_id in self.cart:
            return self.cart[self.product_id]['qty']
        else:
            return 0


    def save(self):
        self.session.modified = True
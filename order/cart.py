class Cart():

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('s_key')
        if 's_key' not in request.session:
            cart = self.session['s_key'] = {}
        self.cart = cart

    def add(self, product):
        product_id = product.id

        if product_id not in self.cart:
            self.cart[product_id] = {'price':product.price}

        self.session.modified = True
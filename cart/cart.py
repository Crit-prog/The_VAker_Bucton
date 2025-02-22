from app.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        # Get request
        self.request = request
        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, no session key!  Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        # product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.productPrice)}
            # self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
      return len(self.cart)

    def get_prods(self):

        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        return products

    def delete(self, product):
        product_id = str(product)
        # Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
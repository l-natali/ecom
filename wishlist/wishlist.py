from django.conf import settings
from base.models import Product


class Wishlist:

    def __init__(self, request):
        """
        Initialize wishlist
        """
        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID)
        if not wishlist:
            # save an empty wishlist in the session
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = {}
        self.wishlist = wishlist

    def add(self, product):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.wishlist:
            self.wishlist[product_id] = {'product': product.title, 'price': str(product.price), }
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.wishlist:
            del self.wishlist[product_id]
            self.save()

    def clear(self):
        # remove wishlist from session
        del self.session[settings.WISHLIST_SESSION_ID]
        self.save()

    def __iter__(self):
        """
        Iterate over the items in the wishlist and get the products from the database.
        """
        product_ids = self.wishlist.keys()
        # get the product objects and add them to the wishlist
        products = Product.objects.filter(id__in=product_ids)
        wishlist = self.wishlist.copy()

        for product in products:
            wishlist[str(product.id)] = product

        for item in wishlist.values():
            yield item

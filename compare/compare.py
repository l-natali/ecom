from django.conf import settings
from base.models import Product


class Compare:

    def __init__(self, request):
        """
        Initialize wishlist
        """
        self.session = request.session
        compare = self.session.get(settings.COMPARE_SESSION_ID)
        if not compare:
            # save an empty compare in the session
            compare = self.session[settings.COMPARE_SESSION_ID] = {}
        self.compare = compare

    def add(self, product):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.compare:
            self.compare[product_id] = {'product': product.title, 'price': str(product.price)}
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.compare:
            del self.compare[product_id]
            self.save()

    def clear(self):
        # remove wishlist from session
        del self.session[settings.COMPARE_SESSION_ID]
        self.save()

    def __iter__(self):
        """
        Iterate over the items in the wishlist and get the products from the database.
        """
        product_ids = self.compare.keys()
        # get the product objects and add them to the wishlist
        products = Product.objects.filter(id__in=product_ids)
        compare = self.compare.copy()

        for product in products:
            compare[str(product.id)] = product

        for item in compare.values():
            yield item

from django.shortcuts import redirect
from django.urls import reverse_lazy
from base.models import Product, CartBanner
from .models import Cart, CartProduct
from base.forms import SubscribeForm
from django.views.generic import TemplateView, View


class AddToCartView(View):

    success_url = reverse_lazy('shop:shop')

    def get(self, request, **kwargs):

        # get product id from requested url
        product_id = self.kwargs['product_id']

        # get product
        product_obj = Product.objects.get(id=product_id)

        # check if cart exist
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)

            # items already exist in cart
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.price
                cartproduct.save()
                cart_obj.total += product_obj.price
                cart_obj.save()

            # new item is added to cart
            else:
                cartproduct = CartProduct.objects.create(
                    cart=cart_obj, product=product_obj, rate=product_obj.price, quantity=1, subtotal=product_obj.price)
                cart_obj.total += product_obj.price
                cart_obj.save()
        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.price, quantity=1, subtotal=product_obj.price)
            cart_obj.total += product_obj.price
            cart_obj.save()

        return redirect('shop:shop')


class ManageCartView(View):
    def get(self, requset, *args, **kwargs):
        item_id = self.kwargs['item_id']
        action = requset.GET.get('action')
        item_obj = CartProduct.objects.get(id=item_id)
        cart_obj = item_obj.cart

        if action == 'inc':
            item_obj.quantity += 1
            item_obj.subtotal += item_obj.rate
            item_obj.save()
            cart_obj.total += item_obj.rate
            cart_obj.save()
        elif action == 'rmv':
            cart_obj.total -= item_obj.subtotal
            cart_obj.save()
            item_obj.delete()
        elif action == 'dcr':
            item_obj.quantity -= 1
            item_obj.subtotal -= item_obj.rate
            item_obj.save()
            cart_obj.total -= item_obj.rate
            cart_obj.save()
            if item_obj.quantity <= 0:
                item_obj.delete()

        return redirect('cart:mycart')


class MyCartView(TemplateView):
    template_name = 'cart.html'

    def post(self, request):
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subscribe = SubscribeForm()
        context['subscribe_form'] = subscribe
        banner = CartBanner.objects.all()
        context['banner'] = banner
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart

        return context


class EmptyCartView(View):
    def get(self, request, *args, **kwargs):
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            cart.cartproduct_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect('cart:mycart')


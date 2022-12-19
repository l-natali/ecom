from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET
from .wishlist import Wishlist
from base.models import Product, WishlistBanner
from cart.models import CartProduct, Cart
from base.forms import SubscribeForm


@require_GET
def wishlist_add(request, product_id):
    wishlist = Wishlist(request)
    product = get_object_or_404(Product, id=product_id)
    wishlist.add(product=product)
    return redirect('shop:shop')


def wishlist_remove(request, product_id):
    wishlist = Wishlist(request)
    product = get_object_or_404(Product, id=product_id)
    wishlist.remove(product)
    return redirect('wishlist:wishlist_detail')


def wishlist_detail(request):
    wishlist = Wishlist(request)
    wishlist_banner = WishlistBanner.objects.all()
    subscribe = SubscribeForm()
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    data = {
        'wishlist': wishlist,
        'cart': cart,
        'banner': wishlist_banner,
        'subscribe_form': subscribe,
    }
    return render(request, 'wishlist.html', context=data)

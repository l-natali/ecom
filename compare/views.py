from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET
from .compare import Compare
from base.models import Product, CompareBanner
from cart.models import CartProduct, Cart
from base.forms import SubscribeForm


@require_GET
def compare_add(request, product_id):
    compare = Compare(request)
    product = get_object_or_404(Product, id=product_id)
    compare.add(product=product)
    return redirect('shop:shop')


def compare_remove(request, product_id):
    compare = Compare(request)
    product = get_object_or_404(Product, id=product_id)
    compare.remove(product)
    return redirect('compare:compare_detail')


def compare_detail(request):

    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    compare = Compare(request)
    compare_banner = CompareBanner.objects.all()
    subscribe = SubscribeForm()
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

    data = {
        'subscribe_form': subscribe,
        'compare': compare,
        'banner': compare_banner,
        'cart': cart,
    }

    return render(request, 'compare.html', context=data)

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Category, Product, ProductPhoto, Advantages, DiscountBanner, Furniture, HomeBanner, Review, Brands
from .models import Contact, AboutBanner, About, Team, FaqBanner, Faq, ShopBanner, ContactBanner
from .models import ProductDetailBanner
from .forms import SubscribeForm, WriteUsForm
from cart.models import CartProduct, Cart
from compare.compare import Compare
from blog.models import Blog
from django.core.paginator import Paginator
from django.views.generic import View, TemplateView
from order.views import NelsonMixin


class BaseView(NelsonMixin, View):

    def get(self, request):
        categories = Category.objects.filter(is_visible=True)
        products = Product.objects.filter(is_visible=True)
        new_arrivals = Product.objects.filter(new_arrival=True)
        advantages = Advantages.objects.all()
        discount_banner = DiscountBanner.objects.all()
        furniture = Furniture.objects.all()
        home_banner = HomeBanner.objects.all()
        product_photo = ProductPhoto.objects.filter(position=1)
        review = Review.objects.all()
        brands = Brands.objects.all()
        contact = Contact.objects.all()
        subscribe = SubscribeForm()
        blog = Blog.objects.all()[:3]
        cart_id = request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None

        data = {'categories': categories,
                'products': products,
                'new_arrivals': new_arrivals,
                'advantages': advantages,
                'discount_banner': discount_banner,
                'furniture': furniture,
                'home_banner': home_banner,
                'product_photo': product_photo,
                'review': review,
                'brands': brands,
                'contact': contact,
                'subscribe_form': subscribe,
                'blog': blog,
                'cart': cart,
                }

        return render(request, 'index.html', context=data)

    def post(self, request):
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.cleaned_data.get('email')
            subscribe.save()
            return redirect('/')


class ShopView(View):

    def get(self, request):
        categories = Category.objects.filter(is_visible=True)
        products = Product.objects.filter(is_visible=True)
        new_arrivals = Product.objects.filter(new_arrival=True)
        shop_banner = ShopBanner.objects.all()
        subscribe = SubscribeForm()
        compare = Compare(request)
        cart_id = request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None

        # Set up Pagination
        p = Paginator(Product.objects.filter(is_visible=True), 15)
        page = request.GET.get('page')
        product_list = p.get_page(page)
        nums = 'a' * product_list.paginator.num_pages

        data = {'categories': categories,
                'products': products,
                'new_arrivals': new_arrivals,
                'shop_banner': shop_banner,
                'subscribe_form': subscribe,
                'cart': cart,
                'compare': compare,
                'product_list': product_list,
                'nums': nums,
                }

        return render(request, 'shop.html', context=data)

    def post(self, request):
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')


class ProductDetails(View):

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug, is_visible=True)
        product_detail_banner = ProductDetailBanner.objects.all()
        subscribe = SubscribeForm()
        cart_id = request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None

        data = {
            'product': product,
            'cart': cart,
            'banner': product_detail_banner,
            'subscribe_form': subscribe,
        }

        return render(request, 'single-product.html', context=data)

    def post(self, request):
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')


class AboutView(View):

    def get(self, request):
        about_banner = AboutBanner.objects.all()
        about = About.objects.all()
        team = Team.objects.all()
        discount_banner = DiscountBanner.objects.all()
        advantages = Advantages.objects.all()
        review = Review.objects.all()
        subscribe = SubscribeForm()
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None

        data = {
            'about_banner': about_banner,
            'about': about,
            'team': team,
            'discount_banner': discount_banner,
            'advantages': advantages,
            'review': review,
            'subscribe_form': subscribe,
            'cart': cart,
        }

        return render(request, 'about.html', context=data)

    def post(self, request):
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')


class FaqView(View):

    def get(self, request):
        faq = Faq.objects.all()
        faq_banner = FaqBanner.objects.all()
        subscribe = SubscribeForm()
        cart_id = request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None

        data = {
            'faq': faq,
            'faq_banner': faq_banner,
            'subscribe_form': subscribe,
            'cart': cart,
        }

        return render(request, 'faq.html', context=data)

    def post(self, request):
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')


class ContactView(View):

    def get(self, request):
        write_us = WriteUsForm()
        contact_banner = ContactBanner.objects.all()
        subscribe = SubscribeForm()
        cart_id = request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None

        data = {'write_us_from': write_us,
                'contact_banner': contact_banner,
                'subscribe_form': subscribe,
                'cart': cart,
                }
        return render(request, 'contact.html', context=data)

    def post(self, request):

        write_us = WriteUsForm(request.POST)
        subscribe = SubscribeForm(request.POST)

        if request.POST.get('form_type') == 'write_us_from':
            write_us.save()
            return redirect('/')
        if request.POST.get('form_type') == 'subscribe_form':
            if subscribe.is_valid():
                subscribe.save()
                return redirect('/')


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get('keyword')
        result = Product.objects.filter(Q(title__icontains=kw) | Q(description__icontains=kw))
        context['result'] = result
        subscribe = SubscribeForm()
        context['subscribe_form'] = subscribe
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart

        return context

    def post(self, request):
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

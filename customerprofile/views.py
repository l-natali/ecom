from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, FormView
from .forms import CustomerRegistrationForm, CustomerLoginForm, PasswordForgotForm, PasswordResetForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from order.views import NelsonMixin
from order.models import Order
from base.forms import SubscribeForm
from cart.models import CartProduct, Cart
from .models import Customer
from .utils import password_reset_token
from base.models import AccountBanner, LoginBanner


class CustomerRegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('my-account')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        if 'next' in self.request.GET:
            next_url = self.request.GET.get('next')
            return next_url
        else:
             return self.success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        login_banner = LoginBanner.objects.all()
        context['banner'] = login_banner
        subscribe = SubscribeForm()
        context['subscribe_form'] = subscribe

        return context


class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class CustomerLoginView(FormView):
    template_name = 'login.html'
    form_class = CustomerLoginForm
    success_url = reverse_lazy('customerprofile:customerprofile')

    def form_valid(self, form):
        uname = form.cleaned_data.get('username')
        pword = form.cleaned_data.get('password')
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Customer.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {
                'form': self.form_class,
                'error': 'Логін або пароль не співпадають!',
            })

        return super().form_valid(form)

    def get_success_url(self):
        if 'next' in self.request.GET:
            next_url = self.request.GET.get('next')
            return next_url
        else:
             return self.success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        login_banner = LoginBanner.objects.all()
        context['banner'] = login_banner
        subscribe = SubscribeForm()
        context['subscribe_form'] = subscribe

        return context


class PasswordForgotView(FormView):
    template_name = 'forgotpassword.html'
    form_class = PasswordForgotForm
    success_url = '/profile/forgot-password/?m=s'

    def form_valid(self, form):
        # get email from user
        email = form.cleaned_data.get('email')
        # get current host ip/domain
        url = self.request.META['HTTP_HOST']
        # get customer and user
        customer = Customer.objects.get(user__email=email)
        user = customer.user
        # send mail to the user with email
        text_content = 'Для зміни паролю перейдіть за посиланням '
        html_content = url + '/profile/password-reset/' + email + '/' + password_reset_token.make_token(user) + '/'
        send_mail(
            'Password Reset Link | Django Ecommerce',
            text_content + html_content,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        login_banner = LoginBanner.objects.all()
        context['banner'] = login_banner
        subscribe = SubscribeForm()
        context['subscribe_form'] = subscribe

        return context


class PasswordResetView(FormView):
    template_name = 'passwordreset.html'
    form_class = PasswordResetForm
    success_url = '/profile/login/'

    def dispatch(self, request, *args, **kwargs):
        email = self.kwargs.get('email')
        user = User.objects.get(email=email)
        token = self.kwargs.get('token')
        if user is not None and password_reset_token.check_token(user, token):
            pass
        else:
            return redirect(reverse('customerprofile:pwdforgot') + '?m=e')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        password = form.cleaned_data['new_password']
        email = self.kwargs.get('email')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        login_banner = LoginBanner.objects.all()
        context['banner'] = login_banner
        subscribe = SubscribeForm()
        context['subscribe_form'] = subscribe

        return context


class CustomerProfileView(NelsonMixin, TemplateView):
    template_name = 'my-account.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/profile/login/?next=/profile/')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        context['customer'] = customer
        orders = Order.objects.filter(cart__customer=customer)
        context['orders'] = orders
        subscribe = SubscribeForm()
        context['subscribe_form'] = subscribe
        account_banner = AccountBanner.objects.all()
        context['banner'] = account_banner
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart

        return context

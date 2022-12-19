"""nelson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base.views import AboutView, SearchView, BaseView, FaqView, ContactView
from blog.views import SearchBlogView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view()),
    path('home/', BaseView.as_view(), name='home'),
    path('shop/', include('base.urls', namespace='shop')),
    path('about/', AboutView.as_view(), name='about'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('compare/', include('compare.urls', namespace='compare')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/', include('customerprofile.urls', namespace='customerprofile')),
    path('manager/', include('manager.urls', namespace='manager')),
    path('search/', SearchView.as_view(), name='search'),
    path('search-blog/', SearchBlogView.as_view(), name='searchblog')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ShopView.as_view(), name='shop'),
    path('<slug:slug>/', views.ProductDetails.as_view(), name='products'),
]

from django.urls import path
from .views import AddToCartView, MyCartView, ManageCartView, EmptyCartView

app_name = 'cart'

urlpatterns = [
    path('add-to-cart-<int:product_id>/', AddToCartView.as_view(), name='addtocart'),
    path('', MyCartView.as_view(), name='mycart'),
    path('manage-cart/<int:item_id>/', ManageCartView.as_view(), name='managecart'),
    path('empty-cart/', EmptyCartView.as_view(), name='emptycart')
]

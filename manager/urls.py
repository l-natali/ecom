from django.urls import path
from .views import ManagerLoginView, ManagerHomeView, ManagerOrderDetailView, ManagerOrderListView, ManagerOdrerStatusChangeView

app_name = 'manager'

urlpatterns = [
    path('login/', ManagerLoginView.as_view(), name='login'),
    path('home/', ManagerHomeView.as_view(), name='home'),
    path('order/<int:pk>/', ManagerOrderDetailView.as_view(), name='orderdetail'),
    path('all-orders/', ManagerOrderListView.as_view(), name='orderlist'),
    path('order-<int:pk>-change/', ManagerOdrerStatusChangeView.as_view(), name='orderstatuschange')
]

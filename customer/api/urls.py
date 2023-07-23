from django.urls import path
from customer.api.views import CustomerRegisterAPIView, LoginAPIView, \
    CustomerOrderListAPIView, CustomerOrderRetrieveAPIView

urlpatterns = [
    path('customer/register/', CustomerRegisterAPIView.as_view(), name='customer-register'),
    path('customer/login/', LoginAPIView.as_view(), name='customer-login'),
    path('orders/', CustomerOrderListAPIView.as_view(), name='customer-orders'),
    path('orders/<int:pk>/', CustomerOrderRetrieveAPIView.as_view(), name='customer-order-detail'),
]

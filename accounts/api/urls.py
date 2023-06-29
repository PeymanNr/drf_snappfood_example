from django.urls import path
from accounts.api.views import CustomerRegisterAPIView, RestaurantRegisterAPIView, LoginAPIView

urlpatterns = [
    path('customer/register/', CustomerRegisterAPIView.as_view(), name='customer-register'),
    path('vendor/register/', RestaurantRegisterAPIView.as_view(), name='restaurant-register'),
    path('vendor/login/', LoginAPIView.as_view(), name='restaurant-login'),
    path('customer/login/', LoginAPIView.as_view(), name='customer-login'),
]

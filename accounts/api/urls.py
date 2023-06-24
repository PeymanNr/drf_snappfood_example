from django.urls import path
from accounts.api.views import CustomerRegisterAPIView, RestaurantRegisterAPIView, LoginAPIView

urlpatterns = [
    path('customer/register/', CustomerRegisterAPIView.as_view(), name='customer-register'),
    path('restaurant/register/', RestaurantRegisterAPIView.as_view(), name='restaurant-register'),
    path('restaurant/login/', LoginAPIView.as_view(), name='restaurant-login'),
    path('customer/login/', LoginAPIView.as_view(), name='customer-login'),

]
from django.urls import path
from accounts.api.views import CustomerRegisterAPIView, RestaurantRegisterAPIView

urlpatterns = [
    path('customer/register/', CustomerRegisterAPIView.as_view(), name='customer-register'),
    path('restaurant/register/', RestaurantRegisterAPIView.as_view(), name='restaurant-register'),

]
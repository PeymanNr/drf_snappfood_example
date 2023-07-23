from django.urls import path
from customer.api.views import LoginAPIView
from restaurants.api.views import RestaurantListAPIView, RestaurantOrderListAPIView, RestaurantOrderRetrieveAPIView, \
    RestaurantRegisterAPIView

urlpatterns = [
    path('list/', RestaurantListAPIView.as_view(), name='restaurants-list'),
    path('orders/', RestaurantOrderListAPIView.as_view(), name='restaurant-orders'),
    path('orders/<int:pk>/', RestaurantOrderRetrieveAPIView.as_view(), name='order-detail'),
    path('vendor/register/', RestaurantRegisterAPIView.as_view(), name='restaurant-register'),
    path('vendor/login/', LoginAPIView.as_view(), name='restaurant-login'),
]


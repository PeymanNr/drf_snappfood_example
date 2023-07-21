from django.urls import path
from restaurants.api.views import RestaurantListAPIView, RestaurantOrderListAPIView, RestaurantOrderRetrieveAPIView

urlpatterns = [
    path('list/', RestaurantListAPIView.as_view(), name='restaurants-list'),
    path('orders/', RestaurantOrderListAPIView.as_view(), name='restaurant-orders'),
    path('orders/<int:pk>/', RestaurantOrderRetrieveAPIView.as_view(), name='order-detail'),
]


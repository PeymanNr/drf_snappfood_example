from django.urls import path
from restaurants.api.views import RestaurantListAPIView

urlpatterns = [
    path('list/', RestaurantListAPIView.as_view(), name='restaurants-list'),
]

from django.urls import path
from accounts.api.views import UserRegistrationCreateAPIView, UserLoginAPIView

urlpatterns = [
    path('register/', UserRegistrationCreateAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),

]
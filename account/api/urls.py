from django.urls import path
from account.api.views import UserRegistrationCreateAPIView, UserLoginAPIView

urlpatterns = [
    path('register/', UserRegistrationCreateAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),

]
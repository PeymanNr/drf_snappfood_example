from django.urls import path
from account.api.views import UserRegistrationCreateAPIView

urlpatterns = [
    path('register/', UserRegistrationCreateAPIView.as_view(), name='user-register'),

]
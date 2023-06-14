from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from account.api.serializers import UserRegisterSerializer

# Create your views here.


class UserRegistrationCreateAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer

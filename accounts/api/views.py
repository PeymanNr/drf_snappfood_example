from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.api.serializers import CustomerRegisterSerializer, RestaurantRegisterSerializer, CustomerLoginSerializer, \
    RestaurantLoginSerializer
from accounts.models import Customer, Restaurant


class CustomerRegisterAPIView(APIView):
    def post(self, request):
        serializer = CustomerRegisterSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            redirect_url = '/customer-dashboard/'
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'redirect_url': redirect_url,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantRegisterAPIView(APIView):
    def post(self, request):
        serializer = RestaurantRegisterSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            redirect_url = '/restaurant-dashboard/'
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'redirect_url': redirect_url,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if Customer.objects.filter(user=user).exists():
            serializer = CustomerLoginSerializer(data=request.data)

        elif Restaurant.objects.filter(user=user).exists():
            serializer = RestaurantLoginSerializer(data=request.data)
        else:
            return Response({'error': 'User Not Register'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# TIP: DO NOT USER PHONE_NUMBER FOR ANY OF REGISTER OR LOGIN TASKS

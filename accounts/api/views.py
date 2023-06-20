# TODO: Add a Register API for customer, the customer can Register with username and password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.api.serializers import CustomerRegisterSerializer, RestaurantRegisterSerializer


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
# TODO: add a Register API for restaurant, the restaurant can Register with username and password


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

# TODO: add a Login API to login Customer and Restaurant by username and password.


# TIP: DO NOT USER PHONE_NUMBER FOR ANY OF REGISTER OR LOGIN TASKS

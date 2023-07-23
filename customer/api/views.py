from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from customer.api.serializers import CustomerRegisterSerializer, CustomerLoginSerializer
from customer.models import Customer, Vendor
from orders.models import Order
from restaurants.api.serializers import OrderDetailSerializer, OrderSerializer, RestaurantLoginSerializer


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


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if Customer.objects.filter(user=user).exists():
            serializer = CustomerLoginSerializer(data=request.data)

        elif Vendor.objects.filter(user=user).exists():
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


class CustomerOrderMixin:
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        customer_id = self.request.user.id
        customer = Customer.objects.get(id=customer_id)
        return Order.objects.filter(customer=customer)


class CustomerOrderListAPIView(CustomerOrderMixin, ListAPIView):
    serializer_class = OrderSerializer


class CustomerOrderRetrieveAPIView(CustomerOrderMixin, RetrieveAPIView):
    serializer_class = OrderDetailSerializer

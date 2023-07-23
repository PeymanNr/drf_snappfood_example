from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from orders.models import Order
from restaurants.api.serializers import RestaurantListSerializer, OrderSerializer, OrderDetailSerializer, \
    RestaurantRegisterSerializer
from restaurants.models import Restaurant


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


class RestaurantListAPIView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['address__city']
    search_fields = ['restaurant__menuitems__name']


class RestaurantOrderMixin:
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        restaurant_id = self.request.user.vendor.restaurant.id
        restaurant = Restaurant.objects.get(id=restaurant_id)
        return Order.objects.filter(restaurant=restaurant)


class RestaurantOrderListAPIView(RestaurantOrderMixin, ListAPIView):
    serializer_class = OrderSerializer


class RestaurantOrderRetrieveAPIView(RestaurantOrderMixin, RetrieveAPIView):
    serializer_class = OrderDetailSerializer


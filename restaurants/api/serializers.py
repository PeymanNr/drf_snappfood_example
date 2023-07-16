from rest_framework import serializers
from accounts.api.serializers import AddressSerializer
from orders.models import Order
from restaurants.models import Restaurant, MenuItem


class RestaurantListSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address')


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'price']


class OrderDetailSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()

    class Meta:
        model = Order
        fields = ['id', 'menu_item', 'quantity', 'total_price']


class OrderSerializer(serializers.Serializer):
    customer = serializers.CharField(source='customer.user.username')

    class Meta:
        model = Order
        fields = ['id', 'customer']


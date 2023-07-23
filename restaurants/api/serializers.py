from django.contrib.auth import authenticate
from rest_framework import serializers
from customer.api.serializers import AddressSerializer
from customer.models import Vendor, User
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


class RestaurantRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    address = AddressSerializer()

    class Meta:
        model = Vendor
        fields = ['password', 'name', 'address']

    def create(self, validated_data):
        password = validated_data['password']
        name = validated_data['name']
        address_data = validated_data['address']

        if Vendor.objects.filter(name=name).exists():
            raise serializers.ValidationError('This username is already in use.')

        user = User.objects.create_user(
            username=self.context['request'].data['username'],
            password=password
        )
        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address = address_serializer.save()

        restaurant = Vendor.objects.create(user=user, name=name, address=address)

        return restaurant


class RestaurantLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')

                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError('Invalid username or password.')
        else:
            raise serializers.ValidationError('Both username and password are required.')


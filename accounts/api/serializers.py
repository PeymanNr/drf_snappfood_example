from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Customer, Restaurant


class CustomerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['password', 'first_name', 'last_name', 'phone', 'address']

    def create(self, validated_data):
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        phone = validated_data['phone']
        address = validated_data['address']

        if Customer.objects.filter(phone=phone).exists():
            raise serializers.ValidationError('این نام کاربری قبلاً استفاده شده است.')

        user = User.objects.create_user(
            username=self.context['request'].data['username'],
            password=password
        )
        customer = Customer.objects.create(user=user, first_name=first_name, last_name=last_name, phone=phone, address=address)
        return customer


class RestaurantRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Restaurant
        fields = ['password', 'name', 'address']

    def create(self, validated_data):
        password = validated_data['password']
        name = validated_data['name']
        address = validated_data['address']

        if Restaurant.objects.filter(name=name).exists():
            raise serializers.ValidationError('این نام کاربری قبلاً استفاده شده است.')

        user = User.objects.create_user(
            username=self.context['request'].data['username'],
            password=password
        )
        restaurant = Restaurant.objects.create(user=user, name=name, address=address)

        return restaurant

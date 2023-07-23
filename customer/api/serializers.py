from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from customer.models import Customer, Vendor
from locations.models import Address, City


class AddressSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', queryset=City.objects.all())

    class Meta:
        model = Address
        fields = ['city', 'description']


class CustomerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    address = AddressSerializer()

    class Meta:
        model = Customer
        fields = ['password', 'first_name', 'last_name', 'phone', 'address']

    def create(self, validated_data):
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        phone = validated_data['phone']
        address_data = validated_data['address']

        if Customer.objects.filter(phone=phone).exists():
            raise serializers.ValidationError('This username is already in use.')

        user = User.objects.create_user(
            username=self.context['request'].data['username'],
            password=password
        )
        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address = address_serializer.save()

        customer = Customer.objects.create(user=user, first_name=first_name, last_name=last_name, phone=phone, address=address)
        return customer


class CustomerLoginSerializer(serializers.Serializer):
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




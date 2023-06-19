from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ('id', 'phone_number', 'password')

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')

        if phone_number and User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('Phone Number is already in use.')

        return attrs

    def create(self, validated_data):
        try:
            validate_password(validated_data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({'password': e.messages})

        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=13)
    password = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'phone_number', 'password']

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        if phone_number and password:
            user = authenticate(phone_number=phone_number, password=password)

            if not user or not user.is_active:
                raise ValidationError("Invalid username or password.")

        else:
            raise serializers.ValidationError('Must include "phone_number" and "password".')
        attrs['user'] = user
        return attrs

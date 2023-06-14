from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from account.models import MyUser


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = MyUser
        fields = ['phone_number', 'password', 'password2']

    def validate(self, attrs):
        validate_password(attrs.get('password'))
        if attrs.get('password') != attrs.get('password2'):
            raise ValidationError('error: passwords are not match')
        attrs.pop('password2')
        return attrs

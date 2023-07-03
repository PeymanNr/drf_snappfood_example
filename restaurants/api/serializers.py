from rest_framework import serializers

from accounts.api.serializers import AddressSerializer
from restaurants.models import Restaurant


class RestaurantListSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address')

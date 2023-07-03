from django.contrib import admin
from django.contrib.admin import register
from restaurants.models import Restaurant


@register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')

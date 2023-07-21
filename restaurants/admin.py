from django.contrib import admin
from django.contrib.admin import register
from restaurants.models import Restaurant, Menu, MenuItem


@register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor')


@register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'restaurant')


@register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
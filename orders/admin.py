from django.contrib import admin
from django.contrib.admin import register
from orders.models import Order


@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'menu_item', 'total_price')

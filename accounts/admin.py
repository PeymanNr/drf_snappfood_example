from django.contrib import admin
from django.contrib.admin import register
from accounts.models import Customer, Vendor
from restaurants.models import MenuItem, Menu


@register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)


@register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
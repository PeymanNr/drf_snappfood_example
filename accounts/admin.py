from django.contrib import admin
from django.contrib.admin import register
from accounts.models import Customer, Vendor


@register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')



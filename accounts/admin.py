from django.contrib import admin
from django.contrib.admin import register
from accounts.models import Customer, Restaurant


@register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@register(Restaurant)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


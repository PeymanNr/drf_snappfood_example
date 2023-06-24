from django.contrib import admin
from django.contrib.admin import register
from accounts.models import Customer, Restaurant


# Register your models here.
@register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@register(Restaurant)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

